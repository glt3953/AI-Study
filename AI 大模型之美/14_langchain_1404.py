import openai, os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

openai.api_key = os.environ.get("OPENAI_API_KEY")

llm = OpenAI(model_name="text-davinci-003", max_tokens=2048, temperature=0.5)

def write_unit_test(function_to_test, unit_test_package = "pytest"):
    # 解释源代码的步骤
    explain_code = """"# How to write great unit tests with {unit_test_package}

    In this advanced tutorial for experts, we'll use Python 3.10 and `{unit_test_package}` to write a suite of unit tests to verify the behavior of the following function.
    ```python
    {function_to_test}
    ```

    Before writing any unit tests, let's review what each element of the function is doing exactly and what the author's intentions may have been.
    - First,"""

    explain_code_template = PromptTemplate(
        input_variables=["unit_test_package", "function_to_test"],
        template=explain_code
    )
    explain_code_llm = OpenAI(model_name="text-davinci-002", temperature=0.4, max_tokens=1000,
            top_p=1, stop=["\n\n", "\n\t\n", "\n    \n"])
    explain_code_step = LLMChain(llm=explain_code_llm, prompt=explain_code_template, output_key="code_explaination")

    # 创建测试计划示例的步骤
    test_plan = """
        
    A good unit test suite should aim to:
    - Test the function's behavior for a wide range of possible inputs
    - Test edge cases that the author may not have foreseen
    - Take advantage of the features of `{unit_test_package}` to make the tests easy to write and maintain
    - Be easy to read and understand, with clean code and descriptive names
    - Be deterministic, so that the tests always pass or fail in the same way

    `{unit_test_package}` has many convenient features that make it easy to write and maintain unit tests. We'll use them to write unit tests for the function above.

    For this particular function, we'll want our unit tests to handle the following diverse scenarios (and under each scenario, we include a few examples as sub-bullets):
    -"""
    test_plan_template = PromptTemplate(
        input_variables=["unit_test_package", "function_to_test", "code_explaination"],
        template= explain_code + "{code_explaination}" + test_plan
    )
    test_plan_llm = OpenAI(model_name="text-davinci-002", temperature=0.4, max_tokens=1000,
            top_p=1, stop=["\n\n", "\n\t\n", "\n    \n"])
    test_plan_step = LLMChain(llm=test_plan_llm, prompt=test_plan_template, output_key="test_plan")

    # 撰写测试代码的步骤
    starter_comment = "Below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator"
    prompt_to_generate_the_unit_test = """

Before going into the individual tests, let's first look at the complete suite of unit tests as a cohesive whole. We've added helpful comments to explain what each line does.
```python
import {unit_test_package}  # used for our unit tests

{function_to_test}

#{starter_comment}"""

    unit_test_template = PromptTemplate(
        input_variables=["unit_test_package", "function_to_test", "code_explaination", "test_plan", "starter_comment"],
        template= explain_code + "{code_explaination}" + test_plan + "{test_plan}" + prompt_to_generate_the_unit_test
    )
    unit_test_llm = OpenAI(model_name="text-davinci-002", temperature=0.4, max_tokens=1000, stop="```")
    unit_test_step = LLMChain(llm=unit_test_llm, prompt=unit_test_template, output_key="unit_test")

    sequential_chain = SequentialChain(chains=[explain_code_step, test_plan_step, unit_test_step],
                                    input_variables=["unit_test_package", "function_to_test", "starter_comment"], verbose=True)
    answer = sequential_chain.run(unit_test_package=unit_test_package, function_to_test=function_to_test, starter_comment=starter_comment)
    return f"""#{starter_comment}""" + answer

code = """
def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours > 0:
        return f"{hours}h{minutes}min{seconds}s"
    elif minutes > 0:
        return f"{minutes}min{seconds}s"
    else:
        return f"{seconds}s"
"""

import ast

def write_unit_test_automatically(code, retry=3):
    unit_test_code = write_unit_test(code)
    all_code = code + unit_test_code
    tried = 0
    while tried < retry:
        try:
            ast.parse(all_code)
            return all_code
        except SyntaxError as e:
            print(f"Syntax error in generated code: {e}")
            all_code = code + write_unit_test(code)
            tried += 1
            
print(write_unit_test_automatically(code))

import openai, os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def gpt35(prompt, model="text-davinci-002", temperature=0.4, max_tokens=1000,
          top_p=1, stop=["\n\n", "\n\t\n", "\n    \n"]):
    response = openai.Completion.create(
        model=model,
        prompt = prompt,
        temperature = temperature,
        max_tokens = max_tokens,
        top_p = top_p,
        stop = stop
        )
    message = response["choices"][0]["text"]
    return message

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

def explain_code(function_to_test, unit_test_package="pytest"):
    prompt = f""""# How to write great unit tests with {unit_test_package}

In this advanced tutorial for experts, we'll use Python 3.10 and `{unit_test_package}` to write a suite of unit tests to verify the behavior of the following function.
```python
{function_to_test}


Before writing any unit tests, let's review what each element of the function is doing exactly and what the author's intentions may have been.
- First,"""
    response = gpt35(prompt)
    return response, prompt

code_explaination, prompt_to_explain_code = explain_code(code)
print(code_explaination)

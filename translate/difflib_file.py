import difflib

#with open('./data/wwdc2019-423-zh.txt') as f:
#    medium_text = f.read()
#
#with open('./data/wwdc2019-423-trans-opus-mt-en-zh.txt') as f:
#    openai_text = f.read()
#
##diff = difflib.ndiff(medium_text.splitlines(keepends=True), openai_text.splitlines(keepends=True))
#diff = difflib.context_diff(medium_text.splitlines(keepends=True), openai_text.splitlines(keepends=True))
#print(''.join(diff), end='')

#diff = difflib.HtmlDiff()
#result = diff.make_file(medium_text.splitlines(), openai_text.splitlines())
#with open('./data/podcast_clip_diff.html', "w") as f:
#    f.write(result)

with open('./data/ChatGPT_Prompt_Engineering_for_Developers-Hgn_trans_en2zh.txt') as f1, open('./data/ChatGPT_Prompt_Engineering_for_Developers-opus-mt-en-zh.txt') as f2:
    diff = difflib.unified_diff(f1.readlines(), f2.readlines())
for line in diff:
    print(line)  # 打印差异内容

import difflib

with open('./data/podcast_clip_medium.txt') as f:
    medium_text = f.read()

with open('./data/podcast_clip_openai.txt') as f:
    openai_text = f.read()

#diff = difflib.ndiff(medium_text.splitlines(keepends=True), openai_text.splitlines(keepends=True))
diff = difflib.context_diff(medium_text.splitlines(keepends=True), openai_text.splitlines(keepends=True))
print(''.join(diff), end='')

#diff = difflib.HtmlDiff()
#result = diff.make_file(medium_text.splitlines(), openai_text.splitlines())
#with open('./data/podcast_clip_diff.html', "w") as f:
#    f.write(result)

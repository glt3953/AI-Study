from pydub import AudioSegment

podcast = AudioSegment.from_mp3("./data/podcast_long.mp3")

# PyDub handles time in milliseconds
#regular_minutes = 15 * 60 * 1000
regular_minutes = 25 * 60 * 1000

total_length = len(podcast)

start = 0
index = 0
while start < total_length:
    end = start + regular_minutes
    if end < total_length:
        chunk = podcast[start:end]
    else:
        chunk = podcast[start:]
    with open(f"./data/podcast_regular_clip_{index}.mp3", "wb") as f:
        chunk.export(f, format="mp3")
    start = end
    index += 1

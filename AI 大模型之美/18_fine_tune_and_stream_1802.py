import pandas as pd

df = pd.read_csv("data/ultraman_stories.csv")
df['sub_prompt'] = df['dynasty'] + "," + df['super_power'] + "," + df['story_type']
prepared_data = df.loc[:,['sub_prompt','story']]
prepared_data.rename(columns={'sub_prompt':'prompt', 'story':'completion'}, inplace=True)
#prepared_data.to_csv('data/prepared_data.csv',index=False)
prepared_data.to_csv('prepared_data.csv',index=False)

import subprocess

subprocess.run('openai tools fine_tunes.prepare_data --file data/prepared_data.csv --quiet'.split())

subprocess.run('openai api fine_tunes.create --training_file data/prepared_data_prepared.jsonl --model curie --suffix "ultraman"'.split())

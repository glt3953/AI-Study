import subprocess

#subprocess.run('openai api fine_tunes.create --training_file data/prepared_data_prepared.jsonl --model curie --suffix "ultraman"'.split())

subprocess.run('openai api fine_tunes.list'.split())

subprocess.run('openai api fine_tunes.results -i ft-3oxkr1zBVB4fJWogJDDjQbr0'.split())

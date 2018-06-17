
import os

import wave
import json
import re

import char_map_generator

# Prepare paths
data_path = 'data'
audio_path = os.path.join(data_path, 'audio-pcm')
transcripts_path = os.path.join(data_path, 'transcripts')
# Gather a list of audio files
files_list = os.listdir(audio_path)

# Open training and validation files for appending
training = open('train_corpus.json', 'a+')
validation = open('valid_corpus.json', 'a+')
# Set current file to training
current_file = training
# Set training data to be 80% of the data
training_limit = len(files_list) * 0.8
# A temporary toggle variable
training = True

# Regex check for the unwanted tags
tag_pattern = re.compile('<[a-z-]+>')
brackets_pattern = re.compile('\(\(\)\)')
punctuation_pattern = re.compile('[*~_<>-]')


def worthy_transcript(text):
    return len(text) > 4

# Return a clean transcript
def clean_transcript(text):
    text = re.sub(tag_pattern, '', text)
    text = re.sub(brackets_pattern, '', text)
    return re.sub(punctuation_pattern, '', text).lower().strip()

# Go over each file, extract data and put into json files
for index, file in enumerate(files_list):
    # Get the transcript
    with open(os.path.join(transcripts_path, file[:-3] + 'txt')) as f:
        # Get rid of the first line which is a timestamp
        f.readline()
        transcript = f.readline()
    transcript = clean_transcript(transcript)
    if worthy_transcript(transcript):
        # Update charset
        char_map_generator.update_set(transcript)
        file_path = os.path.join(audio_path, file)
        # Open the audio file with wave to extract the duration
        audio = wave.open(file_path)
        duration = float(audio.getnframes()) / audio.getframerate()
        # When more than 80% are in training, switch to validation
        if training and index >= training_limit:
            current_file = validation
            training = False
        # Dump the data into the json corpus
        current_file.write(json.dumps({'key': file_path, 'duration': duration, 'text': transcript}, ensure_ascii=False) + '\n')

# Write the charmap into a file
char_map_generator.write_charmap_into_file()

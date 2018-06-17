# Kurdish Language

This repo will be an attempt to try different NLP techniques on the Kurdish Language

The main challenge is that there are only two or three official datasets about this language.

The current work is focused on the speech recognition task.

Short term plan

- [ ] Text Preprocessing
- [ ] Audio Preprocessing
- [ ] Train a simple RNN for this task

Long term goals

- [ ] Build an end to end ASR Pipeline
- [ ] Use a language model


## The Pipeline

1. Get raw .sph files
2. Convert .sph to .wav format [sph to wav converter](./utils/sph-to-wav.sh)
3. Convert .wav to pcm-16 wav [pcm](./utils/convert_audio_pcm.py)
4. Turn audio and transcripts to a json representation [Data Jsonifier](./utils/data_jsonifier.py)
5. Split data into training and validation corpora

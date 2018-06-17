import os

import soundfile as sf

data_path = 'data'


files_list = os.listdir(os.path.join(data_path, 'audio-old'))

for file in files_list:
    data, sample_rate = sf.read(os.path.join(data_path, 'audio-old', file))
    sf.write(os.path.join(data_path, 'audio-pcm', file[:-7] + 'wav'), data, sample_rate)

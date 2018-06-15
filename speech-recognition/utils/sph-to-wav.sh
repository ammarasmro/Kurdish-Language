cd conversational/dev/audio

mkdir wav-audio

for i in *.sph; do
  sph2pipe -f wav $i > wavfiles/$i.wav
done

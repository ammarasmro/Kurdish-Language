# BAD Idea!

cat data/transcripts/*.txt >> data/transcripts/all.txt

for i in *.txt; do
  cat $i >> all.txt
done

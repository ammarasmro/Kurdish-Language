import os

import re

# Pattern to catch time stamps
time_pattern = re.compile('\[.*\]')
# tag_pattern = re.compile('<.*>')
# weird_brackets = re.compile('\(\(\)\)')

char_set = set()
punctuation = set(['*', '~', '(', '_', '<', '>', '-', ')', ' '])

# Open the file with all conversations
with open(os.path.join('..', 'data', 'transcripts', 'all.txt')) as f:
    # Start with an arbitrary value
    line = 'a'
    while line:
        # Remove the trailing newline character and convert to lower case
        line = line.rstrip('\n').lower()
        if not re.match(time_pattern, line) and line != '<no-speech>':
            char_set.update(line)
        line = f.readline()

# Exclude the punctuation from the charset
char_set.difference_update(punctuation)

# Turn charset into a string map
map_string = ''
for num, char in enumerate(sorted(char_set)):
    print(char, num)
    map_string += '{} {}\n'.format(char, num)

# Write the charmap to a file
with open(os.path.join('.','custom_data', 'charmap.txt'), 'w+') as m:
    m.write(map_string)

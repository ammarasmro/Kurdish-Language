"""
Defines two dictionaries for converting
between text and integer sequences.
"""

char_map_str = """
a 0
b 1
c 2
d 3
e 4
f 5
g 6
h 7
i 8
j 9
k 10
l 11
m 12
n 13
o 14
p 15
q 16
r 17
s 18
t 19
u 20
v 21
w 22
x 23
y 24
z 25
ç 26
ê 27
î 28
û 29
ş 30
<SPACE> 31
"""
# the "blank" character is mapped to 32

char_map = {}
index_map = {}
for line in char_map_str.strip().split('\n'):
    ch, index = line.split()
    char_map[ch] = int(index)
    index_map[int(index)+1] = ch
index_map[32] = ' '

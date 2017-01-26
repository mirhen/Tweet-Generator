import random
import sys


words = sys.argv[1:]

random.shuffle(words)
text = ''

for item in words:
    text += " " + item

print text

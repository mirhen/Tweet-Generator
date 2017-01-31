import random
import sys

text = ""

with open('/usr/share/dict/words') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

def random_python_word():

    rand_index = random.randint(0, len(content) - 1)
    return content[rand_index]


num = int(sys.argv[1:][0])

for i in range(num):
    word = random_python_word()
    text += " " + word


print text

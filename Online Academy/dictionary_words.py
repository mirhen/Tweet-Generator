import random
import sys

def random_python_word():

    rand_index = random.randint(0, len(content) - 1)
    return content[rand_index]

def retrieve_words():
    with open('/usr/share/dict/words') as textfile:
        content = textfile.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    text = ""

    if sys.argv[1:][0].isdigit():
        num = int(sys.argv[1:][0])
        if num > len(content) - 1:
            print 'that number is too big'
            num = 0
    else:
        print 'You have to input a number'

    for i in range(num):
        word = random_python_word()
        text += " " + word

    print text


if __name__ == '__main__':
    retrieve_words()

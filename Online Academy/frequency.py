import collections
import random
import operator

text = 'one fish two fish red fish blue fish blue blue blue blue'

def histogram(filename):
    with open(filename,'r') as f:
        content = f.read()
        print content
    content = content.split()
    list2 = {}  #this is a new list
    for word in content:
        if word in list2:
            list2[word] += 1
        else:
            list2[word] = 1
    return list2

def total_words(hist):
    total = 0
    for word in hist:
        total += hist[word]
    return total

def random_number(limit):
    rand_num = random.randint(1, limit)
    return rand_num

def frequency(hist, word):
    total = total_words(hist)

    word = hist[word]
    return float(word)/float(total)

def sochastic(histogram):
    tuples = [(0,'')]
    count = 0
    total =  total_words(histogram)
    print 'There are %s words' % total

    for word in histogram:
        count += histogram[word]
        tuples.append((count, word))
    tuples = sorted(tuples, key=lambda tup: tup[0])
    print tuples

    rand_num = random_number(total)
    j = 0
    print 'rand_num',rand_num

    for x in tuples:
        if j < len(tuples) - 1:
            j += 1
        if x[0] == rand_num:
            return x[1]
        elif  x[0] < rand_num < tuples[j][0]:
            return tuples[j][1]

if __name__ == '__main__':
    hist = histogram('Texts/madeline.txt')

    random_word = sochastic(hist)
    freq = frequency(hist, random_word)
    print '\nUsing Sochastic Sampling \n\nRandom word chosen is', random_word, '\nChance of that word getting chosen:', freq, '\n\n'

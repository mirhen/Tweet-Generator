import collections
import random
import operator
import analyze

def frequency(hist, word):
    total = sum(hist.values())
    word = hist[word]
    return float(word)/float(total)

def sochastic(histogram):
    tuples = [(0,'')]
    count = 0

    for word in histogram:
        count += histogram[word]
        tuples.append((count, word))

    tuples = sorted(tuples, key=lambda tup: tup[0])
    rand_num = random.randint(1, total)
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
    hist = analyze.histogram('Texts/madeline.txt')

    chosen_word = sochastic(hist)
    freq = frequency(hist, chosen_word)
    print '\nUsing Sochastic Sampling \n\nRandom word chosen is', chosen_word, '\nChance of that word getting chosen:', freq, '\n\n'

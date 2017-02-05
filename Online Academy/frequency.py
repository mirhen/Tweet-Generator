import collections

text = 'one fish two fish red fish blue fish'

def histogram(string):
    content = string.split()
    list2 = {}  #this is a new list
    for word in content:
        if word in list2:
            list2[word] += 1
        else:
            list2[word] = 1
    return list2

def total_words(list):
    content = list.split()
    return len(content)

def sample_by_freq(histogram):

    total =  total_words(text)
    print 'There are %s words' % total

    for words in histogram:
        

if __name__ == '__main__':
    hist = histogram(text)
    sample_by_freq(hist)

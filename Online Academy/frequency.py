import collections

a = 'one fish two fish red fish blue fish'

def histogram(string):
    content = string.split()
    list2 = {}  #this is a new list
    for word in content:
        if word in list2:
            list2[word] += 1
        else:
            list2[word] = 1
    return list2


def sample_by_freq(histogram):
    total_words = 0
    for word in histogram:
        total_words += histogram[word]
    print total_words

if __name__ == '__main__':
    hist = histogram(a)
    sample_by_freq(hist)

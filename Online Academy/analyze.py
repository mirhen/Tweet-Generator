import re

def histogram(string):
    content = string.split()
    list2 = {}  #this is a new list
    # with open(filename,'r') as f:
    #     for line in f:
    #         for word in line.split():
    #             word = re.sub('[0123456789!".,:?-]','', word.lower())
    #             content.append(word)

    for word in content:
        if word in list2:
            list2[word] += 1
        else:
            list2[word] = 1

    return list2

def unique_words(hist):
    count = 0
    for word in hist:
        if hist[word] == 1:
            count += 1
    return len(hist)

def frequency(hist, string):
    # if string in hist:
    #     return hist[string]
    # return 0
    # hist.get(string, 0)
    return hist[string] if string in hist else 0

if __name__ == '__main__':
    hist = histogram('Texts/genesis.txt')
    count = unique_words(hist)
    freq = frequency(hist, 'just')
    print count, freq, hist

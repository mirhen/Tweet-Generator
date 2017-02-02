
def histogram(filename):
    content = []
    list2 = {}  #this is a new list
    with open(filename,'r') as f:
        for line in f:
            for word in line.split():
                content.append(word)

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
    return count
def frequency(hist, string):
    return hist[string]


if __name__ == '__main__':
    hist = histogram('madeline.txt')
    count = unique_words(hist)
    freq = frequency(hist, 'the')
    print count, freq

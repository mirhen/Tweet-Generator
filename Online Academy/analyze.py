def histogram():
    graph = {'one': 1}
    words = 'one fish two fish red fish blue fish'
    list1 = words.split()  #this is your original list of words
    list2 = []   #this is a new list

    for word in list1:
        old = word
        if word in list2:
            list2.index(word)[1] += 1
        else:
            list2.append({word:0})

        print list2

def unique_words():

    return 0
def frequency(str):
    return 0


if __name__ == '__main__':
    histogram()

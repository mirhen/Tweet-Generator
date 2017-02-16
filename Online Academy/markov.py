#Markov Model - super dictionary of each word in text , and histogram inside of the super dict, wit the frequency of each words  after the super word.
# "[START]"/"[STOP]"
from histograms import Dictogram

def markov_chain(filename):
    #open textfile
    with open(filename) as textfile:
        content = textfile.read().split()

    # we want one of each word to create the super dictionary with histogram inside of it
    markov_keys = list(set(content))

    # for key in markov_keys:
    # key = "fish"
    tokens_of_super_key = []
    markov_chain = {}
    for key in markov_keys:
        for index, item in enumerate(content):
            if key == item:
                if index != len(content) - 1:
                    token_index = index + 1
                    tokens_of_super_key.append(content[token_index])

        markov_chain[key] = Dictogram(tokens_of_super_key)
        tokens_of_super_key = []
    print markov_chain





if __name__ == '__main__':
    import sys

    arg = sys.argv[1:]
    if arg == []:
        markov_chain('fish0.txt')
        

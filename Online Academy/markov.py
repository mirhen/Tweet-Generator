#Markov Model - super dictionary of each word in text , and histogram inside of the super dict, wit the frequency of each words  after the super word.
# "[START]"/"[STOP]"
from histograms import Dictogram
import sample
import cleanup
def markov_chain(filename):
    #transform and cleanup textfile
    content = cleanup.clean(filename)

    # we want one of each word to create the super dictionary with histogram inside of it
    markov_keys = list(set(content))

    tokens_of_super_key = []
    markov_chain = {}
    start_list = []
    for key in markov_keys:
        for index, item in enumerate(content):
            if key == item:
                if index != len(content) - 1:
                    if index - 1 == -1:
                        start_list.append(content[index])
                    elif '.' in item:
                        content[index] = item.replace('.', '')
                        token_index  = index + 1
                        start_list.append(content[token_index])
                        tokens_of_super_key.append(content[token_index].replace)
                    else:
                        token_index = index + 1
                        tokens_of_super_key.append(content[token_index])

        markov_chain[key] = Dictogram(tokens_of_super_key)
        tokens_of_super_key = []

    markov_chain['[START]'] = Dictogram(start_list)
    # clean_markov_chain = { x.replace('.', ''): markov_chain[x] for x in markov_chain.keys() }

    return markov_chain

def generate_sentence(markov_chain, length_of_sentence):
    sentence = ''
    word = ''
    for i in range(length_of_sentence):
        if sentence == '':
            rand_word = sample.sample_word(markov_chain['[START]'])
            word = rand_word
            sentence += rand_word
        elif sentence != '':
                rand_word = sample.sample_word(markov_chain[word])
                sentence += ' ' + rand_word
                word = rand_word
    return sentence


if __name__ == '__main__':
    import sys

    arg = sys.argv[1:]
    filename = arg[0]
    markov_dict = markov_chain(filename)

    if len(arg) == 0:
        markov_dict = markov_chain('fish0.txt')
    elif len(arg) == 1:
        sentence = generate_sentence(markov_dict, 4)
        print sentence
    elif len(arg) == 2:
        length_of_sentence = arg[1]
        if length_of_sentence.isdigit():
            sentence = generate_sentence(markov_dict, int(length_of_sentence))
            print sentence
        else:
            print 'Type length of sentence, not', length_of_sentence

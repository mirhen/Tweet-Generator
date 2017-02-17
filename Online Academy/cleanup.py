import re

def clean(filename):
    #open textfile
    with open(filename) as textfile:
        raw_content = textfile.read().split()
        content = []
        for word in raw_content:
            word = re.sub('[0123456789!",:?-]','', word)
            content.append(word)
    return content

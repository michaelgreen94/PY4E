filename = input('file:')
document = open(filename, 'r')

dictionary = dict()
for line in document:
    words = line.split()
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

biggestword = None
biggestcounter = None
for word, count in dictionary.items():
    if biggestcounter is None or count > biggestcounter:
        biggestcounter = count
        biggestword = word

print(biggestword+':', biggestcounter)

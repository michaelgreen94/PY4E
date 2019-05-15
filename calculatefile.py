filename = input('file: ')
document = open(filename, 'r+')

charges = dict()
for line in document:
    words = line.split('\t')
    chargeType = words[2]
    charge = words[4].replace('$', '')
    charges[chargeType] = charges.get(chargeType, 0) + float(charge)

document.write('\n\n')
for x, y in charges.items():
    newline = x + '\t' + str(y) + '\n'
    document.write(newline)

document.close()

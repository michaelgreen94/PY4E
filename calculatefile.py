filename = input('file: ')
document = open(filename, 'r+')

charges = dict()
for line in document:
    words = line.split('\t')
    chargeType = words[2]
    charge = words[4].replace('$', '')
    charges[chargeType] = charges.get(chargeType, 0) + float(charge)

print(str(charges))
# document.write('\n')
# for x, y in charges.items():
#     newline = str(x, y)
#     document.write(newline)

# document.close()

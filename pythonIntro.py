# print a countdown
for countdown in 5, 4, 3, 2, 1, 'hey!':
    print(countdown)

# prints selected string from list
list = [
    'day one',
    'day 2',
    'day three',
    'day 4our',
    'thought it was gonna be day five huh?',
]
print(list[4])

# prints value using key
quotes = {
    'Aly': 'Ouch my FOOT!',
    'Liam': 'Can I have a snack?',
    'Olivia': '*grunts*'
}
person = 'Olivia'
print(person, 'says:', quotes[person])

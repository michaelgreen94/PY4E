# print a countdown
# for countdown in 5, 4, 3, 2, 1, 'hey!':
#     print(countdown)

# prints selected string from list
# list = [
#     'day one',
#     'day 2',
#     'day three',
#     'day 4our',
#     'thought it was gonna be day five huh?',
# ]
# print(list[4])
# this uses [] brakets to make a list

# prints value using key
# quotes = {
#     'Aly': 'Ouch my FOOT!',
#     'Liam': 'Can I have a snack?',
#     'Olivia': '*grunts*'
# }
# person = 'Olivia'
# print(person, 'says:', quotes[person])
# this uses {} brackets to make a dictionary, can also create an empty dictionary using dict()

# first funcitonal program from book. I didnt write this.
# import webbrowser
# import json
# from urllib.request import urlopen

# print('lets find an old website.')
# site = input('Type the URL: ')
# time = input('give me a year, month, day like 20150613: ')
# url = 'http://archive.org/wayback/available?url=%s&timestamp=%s' % (site, time)
# response = urlopen(url)
# contents = response.read()
# text = contents.decode('utf-8')
# data = json.loads(text)

# try:
#     old_site = data['archived_snapshots']['closest']['url']
#     print('Found this copy: ', old_site)
#     print('It should appear in your browser now')
#     webbrowser.open(old_site)
# except:
#     print('Sorry, no luck finding', site)

# language = 1
# print('language %s: I am Python. Whats for supper?' % (language + 10))
# this is interesting, im not sure what the %s is for, but I see what its doing. Ill look more into this.

# int('101') will converto to
# 101
# while int('101.0') will throw an error.
# Use float('101.0') to convert a string to a "float"
# just remember to use common data types and all will be good xD

# start = 'Na ' * 4 + '\n'
# middle = 'hey ' * 3 + '\n'
# end = 'goodbye.'
# print(start + start + middle + end)
# * tells it to duplicate the previous string this many times

# letters = 'abcdefghijklmnopqrstuvwxyz'
# # prints the 16th letter in the string!
# print(letters[15])
# # using a "-" will count from the end forward
# print(letters[-9])

# name = 'Mike'
# name = name.replace('M', 'P')
# name = 'P' + name[1:]
# print(name)

# lets try fibonacci
# def fib(n):
#     x, y = 0, 1
#     while x < n:
#         print(x, end=' ')
#         x, y = y, x + y
# fib(1000)


# secperhour = 60 * 60 * 60
# secperday = secperhour * 24
# hoursperday = secperday / secperhour
# x = secperday // secperday
# print(secperhour, secperday, hoursperday, x)

# solve for palindrome
# x = 0
# palindromes = {}
# length = int(input('how many do you want to test?: '))
# if type(length) is int:
#     while x < length:
#         userInput = input('give me a word: ')
#         reverseInput = userInput[::-1]
#         if userInput == reverseInput:
#             palindromes[userInput] = True
#             print('yay you found one!')
#         else:
#             palindromes[userInput] = False
#             print(reverseInput, 'isnt quite', userInput, 'backwards')
#         x += 1
# else:
#     print('run me again but use a number')
# print(palindromes)

# houses = dict()
# x = 10
# y = 20
# houses[x, y] = 'myhouse'
# print(houses)

# years_list = [1994, 1995, 1996, 1997, 1998, 1999]
# my_third_birthday = years_list[3]
# oldest = years_list[-1]
# print(years_list, my_third_birthday, oldest)

# things = ['mozzarella', 'cinderella', 'salmonella']
# print(things)
# things[1] = things[1].capitalize()
# things[0] = things[0].upper()
# del things[2]
# OR things.remove('salmonella')
# print(things)

# surprise = ['Groucho', 'Chico', 'harpo']
# surprise[-1] = surprise[-1].lower()[::-1].capitalize()
# print(surprise)

# e2f = {
#     'dog': 'chien',
#     'cat': 'chat',
#     'walrus': 'morse'
# }
# print(e2f['walrus'])

# f2e = {}
# for english, french in e2f.items():
#     f2e[french] = english
# print(f2e['chien'])

# englishSet = set(e2f.keys())
# print(englishSet)

# life = dict()
# list_of_names = ['Henri', 'Grumpy', 'Lucy']
# animals = dict()
# animals['cats'] = list_of_names
# animals['octopi'] = dict()
# animals['emus'] = dict()
# life['animals'] = animals
# life['plants'] = dict()
# life['other'] = dict()

# correct way
# life = {
#   'animals': {
#     'cats': [
#       'Henri', 'Grumpy', 'Lucy'
#     ],
#     'octopi': {},
#     'enums': {}
#   },
#   'plants': {},
#   'other': {}
# }

# print(life.keys())
# print(list(life['animals'].keys()))
# print(list(life['animals']['cats']))

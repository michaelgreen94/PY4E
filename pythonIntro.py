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
#   old_site = data['archived_snapshots']['closest']['url']
#   print('Found this copy: ', old_site)
#   print('It should appear in your browser now')
#   webbrowser.open(old_site)
# except:
#   print('Sorry, no luck finding', site)

# language = 1
# print('language %s: I am Python. Whats for supper?' % (language + 10))
# this is interesting, im not sure what the %s is for, but I see what its doing. Ill look more into this.

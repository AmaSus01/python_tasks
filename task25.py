import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/088.txt')

print(len(r.text))
counter = 0

for i in r.text:
    if i == '\n':
        counter += 1

print('Result: ', counter)

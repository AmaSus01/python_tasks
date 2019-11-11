import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
k = r.text
while True:
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + k)
    k = r.text
    print(k)
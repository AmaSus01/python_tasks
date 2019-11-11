s = input().lower().split()
d = {}
for i in s:
    d[i] = s.count(i)
for key, item in d.items():
    print(key, item)


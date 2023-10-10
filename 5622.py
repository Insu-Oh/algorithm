u = input()

c = len(u)
for i in u:
    c += (ord(i) - ord('A') + 6)//3
    if i in 'SVYZ': c-=1

print(c)



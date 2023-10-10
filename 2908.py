n1, n2 = input().split()

n1 = ''.join(reversed(n1))
n2 = ''.join(reversed(n2))

print(max(int(n1), int(n2)))


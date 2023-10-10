import sys

S = sys.stdin.readline()

alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

for i in alphabet:
    for j in range(0, len(S)):
        if not i in S:
            print(-1)
            break
        elif i == S[j]:
            print(j)
            break

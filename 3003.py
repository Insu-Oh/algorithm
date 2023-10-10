# 킹1, 퀸1, 비숍2, 나이트2, 폰8 => 8

a = list(map(int, input().split()))

r = [1, 1, 2, 2, 2, 8]

result = list()
for i in range(len(r)):
    result.append(str(r[i]-a[i]))
    
for i in result:
    print(i, end=' ')
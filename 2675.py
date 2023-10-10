import sys


# INPUT
quantity = int(sys.stdin.readline())

user_inputs = list()
for i in range(quantity):
    user_inputs.append(sys.stdin.readline().strip())


# OUTPUT
for u in user_inputs:
    quantity = int(u.split(' ')[0])
    word = u.split(' ')[1]
    
    completed_letter = ''

    for w in (word):
        for q in range(quantity):
            completed_letter += w
    print(completed_letter)




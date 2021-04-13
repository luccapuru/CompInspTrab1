import random

m = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1],
]

pm =  0.02

for i1, i in enumerate(m):
    for j in range(len(i)):
        #print("teste")
        if random.random() <= pm:
            print("oi", i1, j)
            if i[j] == 0:
                i[j] = 1
            else: 
                i[j] = 0

print(m)
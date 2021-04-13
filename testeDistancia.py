import random
def Distancia(m, l):
    dist = [0, 0, 0, 0, 0, 0, 0, 0]
    for i,lista in enumerate(m):
        for j,num in enumerate(lista):
            if m[i][j] != l[j]:
                print(m[i][j], l[j])
                print(m[i][j], l[i])
                dist[i] += 1
    return dist

m = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
for i,lista in enumerate(m):
    for j,num in enumerate(lista):
        m[i][j] = random.randint(0,1)

lt = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]

print("M:", m)
print(Distancia(m, lt))
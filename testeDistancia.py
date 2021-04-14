import random
def Distancia(m, l):
    dist = [0, 0, 0, 0, 0, 0, 0, 0]
    for i,lista in enumerate(m):
        for j,num in enumerate(lista):
            if m[i][j] != l[j]:
                #print(m[i][j], l[j])
                #print(m[i][j], l[i])
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
dist = Distancia(m, lt)
print("d", dist)

#pop = []
#for i in range(len(dist)):
    #sorteio = random.sample(range(len(dist)), 3)
    #print(sorteio)
    #if dist[sorteio[0]] >= dist[sorteio[1]] and dist[sorteio[0]] >= dist[sorteio[2]]:
        #pop.append(sorteio[0])
    #elif dist[sorteio[1]] >= dist[sorteio[0]] and dist[sorteio[1]] >= dist[sorteio[2]]:
       # pop.append(sorteio[1])
    #elif dist[sorteio[2]] >= dist[sorteio[1]] and dist[sorteio[2]] >= dist[sorteio[0]]:
        #pop.append(sorteio[2])

soma = 0
distaux = 0
for i in dist:
    soma += i
dist1 = []
pop = []
for i in range(len(dist)):
    distaux += round(dist[i]*360/soma)
    dist1.append(distaux)
print(dist1)
sorteio = random.randint(0, 90)
#print("Sorteio 0", sorteio)
esp = 360/len(dist)
#agulhas = []
for i in range(len(dist)):
    print("Sorteio", i, sorteio)
    for j in range(len(dist)):
        if sorteio < dist1[j]:
            pop.append(j)
            break
    sorteio += esp
    if sorteio > 360:
        sorteio -= 360

print(pop)
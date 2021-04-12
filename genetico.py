import random
import math

def PopulacaoRandom():
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
    return m

def Distancia(m, l):
    dist = [0, 0, 0, 0, 0, 0, 0, 0]
    for i,lista in enumerate(m):
        for j,num in enumerate(lista):
            if m[i][j] != l[i]:
                dist[i] += 1
    return dist

def Roleta(dist):
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
    for i in range(len(dist)):
        sorteio = random.randint(0, 360)
        print(sorteio)
        for j in range(len(dist)):
            if sorteio < dist1[j]:
                pop.append(j)
                break
    return pop

def AtualizaPop(pop, m):
    m1 = [] 
    for i in range(len(m)):
        m1.append(m[pop[i]])
    return m1

def Reproducao(pop, m):
    pc = 0.6 #taxa de crossover
    crosspares = []
    for i in range(4):
        if random.random() <= pc:
            crosspares.append(i)
    print("CP:", crosspares)
    cp = None 
    for i in range(len(crosspares)):
        
    return crosspares


    



matriz = PopulacaoRandom()
print(matriz)
lt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d = Distancia(matriz, lt)
print("D", d)
pop = Roleta(d)
#print(Roleta(d))
matriz = AtualizaPop(pop, matriz)
print("M:", matriz)
print(Reproducao(pop, matriz))

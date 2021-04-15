import random
import math
import copy

#inicia a matriz da populacao
def PopulacaoRandom():
    m = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for i,lista in enumerate(m):
        for j,num in enumerate(lista):
            m[i][j] = random.randint(0,1)
    return m

#calculo de distancia entre a um individuo da populacao e a bitstring desejada
#def Distancia(m, l):
    #dist = [0, 0, 0, 0, 0, 0, 0, 0]
    #for i,lista in enumerate(m):
        #for j,num in enumerate(lista):
            #if m[i][j] != l[j]:
                #dist[i] += 1
    #return dist

def Aptidao(m):
    apt = []
    x = 0
    for i in range(len(m)):
        for j in range(len(m)):
            x += m[i][j]*math.pow(2,-j-1)
        fx = CalcFunc(x)
        apt.append(fx)
        x = 0
    return apt
        

def CalcFunc(x):
    result = 2**(-2*((x-0.1)/0.9)**2) * (math.sin(5*math.pi*x))**6
    return result

#selecao por roleta
def Roleta(dist):
    soma = 0
    distaux = 0
    for i in dist:
        soma += i
    dist1 = []
    pop = []
    for i in range(len(dist)):
        distaux += math.ceil((dist[i]/soma)*360)
        dist1.append(distaux)
    print(dist1)
    for i in range(len(dist)):
        sorteio = random.randint(0, 360)
        print(sorteio)
        for j in range(len(dist)):
            if sorteio <= dist1[j]:
                pop.append(j)
                break
    print("Pop", pop)
    #for i in range(len(m)):
        #m[i] = m[pop[i]]
    #print("M mod:", m)
    return pop

def Torneio(dist):
    pop = []
    for i in range(len(dist)):
        sorteio = random.sample(range(len(dist)), 3)
        print(sorteio)
        if dist[sorteio[0]] >= dist[sorteio[1]] and dist[sorteio[0]] >= dist[sorteio[2]]:
            pop.append(sorteio[0])
        elif dist[sorteio[1]] >= dist[sorteio[0]] and dist[sorteio[1]] >= dist[sorteio[2]]:
            pop.append(sorteio[1])
        elif dist[sorteio[2]] >= dist[sorteio[1]] and dist[sorteio[2]] >= dist[sorteio[0]]:
            pop.append(sorteio[2])
    return pop

def SUS(dist):
    soma = 0
    distaux = 0
    for i in dist:
        soma += i
    dist1 = []
    pop = []
    for i in range(len(dist)):
        distaux += math.ceil((dist[i]/soma)*360)
        dist1.append(distaux)
    print(dist1)
    sorteio = random.randint(0, 90)
    #print("Sorteio 0", sorteio)
    esp = 360/len(dist)
    #agulhas = []
    for i in range(len(dist)):
        print("Sorteio", i, sorteio)
        for j in range(len(dist)):
            if sorteio <= dist1[j]:
                pop.append(j)
                break
        sorteio += esp
        if sorteio > 360:
            sorteio -= 360
    return pop

def Crossover(l, q):
    cp = random.randint(0, len(l)-1) #ponto de crossover
    #print(l)
    #print(q)
    #print("Ponto de crossover:", cp)
    for i in range(cp, len(l)):
        l[i], q[i] = q[i], l[i]
    #print(l)
    #print(q, "\n\n")
    return l, q

def Mutacao(pm, m):
    for i1,i in enumerate(m):
        for j in range(len(i)):
            if random.random() <= pm:
                print("oi", i1, j)
                if i[j] == 0:
                    i[j] = 1
                else: 
                    i[j] = 0

def Reproducao(pop, m, pc):
    m1 = [] 
    #pc = 0.6 #taxa de crossover*
    crosspares = []
    for i in range(int(float(len(pop))/2)): #montando pares
        crosspares.append((pop[2*i], pop[2*i+1]))
    print("CP:", crosspares) 
    for i in range(len(crosspares)):
        if(random.random() <= pc):
            #m1[crosspares[i][0]], m1[crosspares[i][1]] = Crossover(m[crosspares[i][0]], m[crosspares[i][1]])
            #print("Cross", i)
            maux = copy.deepcopy(m)
            maux[crosspares[i][0]], maux[crosspares[i][1]] = Crossover(maux[crosspares[i][0]], maux[crosspares[i][1]])
            m1.append(copy.deepcopy(maux[crosspares[i][0]]))
            m1.append(copy.deepcopy(maux[crosspares[i][1]]))
        else:
            #print("NCross", i)
            m1.append(copy.deepcopy(m[crosspares[i][0]]))
            #print(crosspares[i][0], m[crosspares[i][0]])
            m1.append(copy.deepcopy(m[crosspares[i][1]]))
            #print(crosspares[i][1], m[crosspares[i][1]], "\n\n")
    #print("M::", m)
    return m1

def Genetico(pc, pm, maxGen):
    m = PopulacaoRandom() #gera uma populacao inicial aleatoria
    h = Aptidao(m) #calcula a distancia de Hamming da pop atual até a bitstring desejada (aptidao)
    besth = max(h)
    bestx = m[h.index(besth)]
    hMedio = []
    hMedio.append(sum(h)/len(h)) #calcula aptidao media da geracao
    gen = 0
    print("h:", h)
    print("hMedio:", hMedio)
    print("Gen:", gen)
    while gen < maxGen and 1.0 not in h: #Condicao de Parada: Max de geracoes e aptidao 
        #pop = Roleta(h) #selecao por roleta #retorna os indices da nova populacao
        #pop = Torneio(h)
        pop = SUS(h)
        m = Reproducao(pop, m, pc)
        Mutacao(pm, m)
        h = Aptidao(m)
        hMedio.append(sum(h)/len(h))
        gen += 1
        print("h:", h)
        print("M:", m)
        #print("hMedio:", hMedio)
        print("Gen:", gen)
        if besth < max(h):
            besth = max(h)
            bestx = m[h.index(besth)]
    print("BH:", besth)
    print("BX:", bestx)
    return m 

#lt = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
#lt = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
taxaMutacao = input("Digite a taxa de mutacao: ")
taxaCross = input("Digite a taxa de Crossover: ")
maxGen = input("Digite o maximo de geracoes: ")
print(Genetico(float(taxaCross), float(taxaMutacao), int(maxGen)))

import random
import math
import copy
import matplotlib.pyplot as plt
import matplotlib

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

def CalcX(lista):
    x = 0
    for j in range(len(lista)):
        x += lista[j]*math.pow(2,-j-1)
    return x


#calculo de distancia entre a um individuo da populacao e a bitstring desejada
#def Distancia(m, l):
    #dist = [0, 0, 0, 0, 0, 0, 0, 0]
    #for i,lista in enumerate(m):
        #for j,num in enumerate(lista):
            #if m[i][j] != l[j]:
                #dist[i] += 1
    #return dist

def Aptidao(m):
    apt = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(m)-1):
        x = CalcX(m[i])
        fx = CalcFunc(x)
        apt[i] = fx
    return apt
        

def CalcFunc(x):
    result = 2**(-2*((x-0.1)/0.9)**2) * (math.sin(5*math.pi*x))**6
    return result

#selecao por roleta
def Roleta(dist, distMax):
    soma = 0
    distaux = 0
    for i in dist:
        soma += i
    soma += distMax
    dist1 = []
    pop = []
    for i in range(len(dist)):
        distaux += math.ceil((dist[i]/soma)*360)
        dist1.append(distaux)
    distaux += round(distMax*360/soma)
    dist1.append(distaux)
    for i in range(len(dist)):
        sorteio = random.randint(0, 360)
        print(sorteio)
        for j in range(len(dist1)):
            if sorteio <= dist1[j]:
                pop.append(j)
                break
    return pop

def Torneio(dist, distMax):
    pop = []
    dist.append(distMax)
    print(dist)
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

def SUS(dist, distMax):
    soma = 0
    distaux = 0
    for i in dist:
        soma += i
    soma += distMax
    dist1 = []
    pop = []
    for i in range(len(dist)):
        distaux += math.ceil((dist[i]/soma)*360)
        dist1.append(distaux)
    distaux += round(distMax*360/soma)
    dist1.append(distaux)
    sorteio = random.randint(0, 90)
    esp = 360/len(dist)
    #agulhas = []
    for i in range(len(dist)):
        for j in range(len(dist1)):
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
    m1.append(copy.deepcopy(m[len(m)-1]))
    return m1

def Genetico(pc, pm, maxGen, k):
    kaux = k
    m = PopulacaoRandom() #gera uma populacao inicial aleatoria
    h = Aptidao(m) #calcula a distancia de Hamming da pop atual até a bitstring desejada (aptidao)
    besth = max(h)
    bestx = m[h.index(besth)]
    hMedio = []
    hMax = []
    hMedio.append(sum(h)/len(h)) #calcula aptidao media da geracao
    gen = 0
    print("h:", h)
    print("hMedio:", hMedio)
    print("Gen:", gen)
    while gen < maxGen and 1.0 not in h and k >= 0: #Condicao de Parada: Max de geracoes e aptidao 
        #pop = Roleta(h, besth) #selecao por roleta #retorna os indices da nova populacao
        #pop = Torneio(h, besth)
        pop = SUS(h, besth)
        m.append(bestx)
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
            k = kaux
        else: 
            k -= 1
        hMax.append(besth)
    print("BH:", besth)
    print("BX:", bestx, CalcX(bestx))
    print("GenBest:", m[h.index(max(h))], CalcX(m[h.index(max(h))]))
    fig, ax = plt.subplots()
    ax.plot(range(len(hMedio)), hMedio, label = "Aptidão Média")
    ax.plot(range(len(hMax)), hMax, label = "Aptidão Máxima")
    ax.set_xlabel("Gerações")  
    ax.set_ylabel("Aptidão")
    ax.legend()
    matplotlib.pyplot.savefig("teste2")
    return m 

#lt = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
#lt = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
taxaMutacao = input("Digite a taxa de mutacao: ")
taxaCross = input("Digite a taxa de Crossover: ")
maxGen = input("Digite o maximo de geracoes: ")
maxk = input("Digite o numero max de iteracoes para convergencia: ")
print(Genetico(float(taxaCross), float(taxaMutacao), int(maxGen), int(maxk)))

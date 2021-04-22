import random
import math
import copy
import matplotlib.pyplot as plt
import matplotlib
#import numpy as np

#inicia a matriz da populacao
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

#calculo de distancia entre a um individuo da populacao e a bitstring desejada
def Distancia(m, l):
    dist = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(m)-1):
        for j in range(len(m[i])):
            if m[i][j] != l[j]:
                dist[i] += 1
    return dist

#selecao por roleta
def Roleta(dist, distMax):
    #soma os valores para criar um lista da roleta
    soma = 0
    distaux = 0
    for i in dist:
        soma += i
    soma += distMax
    dist1 = []
    pop = [] #cria lista da populacao
    for i in range(len(dist)):
        distaux += math.ceil(dist[i]*360/soma)
        dist1.append(distaux)
    distaux += math.ceil(distMax*360/soma)
    dist1.append(distaux)
    #sorteia a nova populacao e retorna
    for i in range(len(dist)):
        sorteio = random.randint(0, 360)
        for j in range(len(dist1)):
            if sorteio <= dist1[j]:
                pop.append(j)
                break
    return pop

#seleção por torneio
def Torneio(dist, distMax):
    pop = [] #cria lista da populacao
    dist.append(distMax)
    for i in range(len(dist)):
        sorteio = random.sample(range(len(dist)), 3) #sorteio 1x1x1
        if dist[sorteio[0]] >= dist[sorteio[1]] and dist[sorteio[0]] >= dist[sorteio[2]]:
            pop.append(sorteio[0])
        elif dist[sorteio[1]] >= dist[sorteio[0]] and dist[sorteio[1]] >= dist[sorteio[2]]:
            pop.append(sorteio[1])
        elif dist[sorteio[2]] >= dist[sorteio[1]] and dist[sorteio[2]] >= dist[sorteio[0]]:
            pop.append(sorteio[2])
    return pop

#seleção por amostragem universal estocástica => pareciod com Roleta
def SUS(dist, distMax):
    soma = 0
    distaux = 0
    for i in dist:
        soma += i
    soma += distMax
    dist1 = []
    pop = [] #criação da lista de população
    for i in range(len(dist)):
        distaux += math.ceil(dist[i]*360/soma)
        dist1.append(distaux)
    distaux += math.ceil(distMax*360/soma)
    dist1.append(distaux)
    sorteio = random.randint(0, 90) #sorteia no primeiro quadrante e some 360/numero de agulhas na roleta para achar os outros
    esp = 360/len(dist)
    for i in range(len(dist)):
        for j in range(len(dist1)):
            if sorteio <= dist1[j]:
                pop.append(j)
                break
        sorteio += esp
        if sorteio > 360:
            sorteio -= 360
    return pop

#operação de CrossOver
def Crossover(l, q):
    cp = random.randint(0, len(l)-1) #ponto de crossover
    for i in range(cp, len(l)):
        l[i], q[i] = q[i], l[i]
    return l, q

#Operação de mutação
def Mutacao(pm, m):
    for i1,i in enumerate(m):
        for j in range(len(i)):
            if random.random() <= pm:
                if i[j] == 0:
                    i[j] = 1
                else: 
                    i[j] = 0

#cria a matriz com a nova população já com CrossOver
def Reproducao(pop, m, pc):
    m1 = [] 
    crosspares = []
    for i in range(int(float(len(pop))/2)): #montando pares
        crosspares.append((pop[2*i], pop[2*i+1]))
    for i in range(len(crosspares)):
        if(random.random() <= pc):
            maux = copy.deepcopy(m)
            maux[crosspares[i][0]], maux[crosspares[i][1]] = Crossover(maux[crosspares[i][0]], maux[crosspares[i][1]])
            m1.append(copy.deepcopy(maux[crosspares[i][0]]))
            m1.append(copy.deepcopy(maux[crosspares[i][1]]))
        else: #se não houver crossover, somente passar os filhos para frente
            m1.append(copy.deepcopy(m[crosspares[i][0]]))
            m1.append(copy.deepcopy(m[crosspares[i][1]]))
    m1.append(copy.deepcopy(m[len(m)-1])) #elitismo
    return m1

#Algoritmo principal
def Genetico(bitstring, pc, pm, maxGen):
    m = PopulacaoRandom() #gera uma populacao inicial aleatoria
    h = Distancia(m, bitstring) #calcula a distancia de Hamming da pop atual até a bitstring desejada (aptidao)
    besth = max(h) #salva melhor aptidão
    bestx = m[h.index(besth)] #salva melhor individuo
    m.append(bestx) #elitismo
    hMedio = [] #lista para plot do gráfico
    hMax = [] # """"""
    hMedio.append((sum(h)+besth)/(len(h)+1)) #calcula aptidao media da geracao
    hMax.append(max(h)) 
    gen = 0
    while gen < maxGen and 12 not in h: #Condicao de Parada: Max de geracoes e aptidao 
        #pop = Roleta(h, besth) #selecao por roleta #retorna os indices da nova populacao
        #pop = Torneio(h, besth)  #selecao por torneio #retorna os indices da nova populacao
        pop = SUS(h, besth)  #selecao por amostra estocástica #retorna os indices da nova populacao
        m[len(m)-1] = copy.deepcopy(bestx)
        m = Reproducao(pop, m, pc)
        Mutacao(pm, m)
        h = Distancia(m, bitstring)
        hMedio.append((sum(h)+besth)/(len(h)+1))
        gen += 1
        if besth < max(h):
            besth = max(h)
            bestx = m[h.index(besth)]
        hMax.append(besth)
    #plot do gráfico
    #fig, ax = plt.subplots()
    #ax.plot(range(len(hMedio)), hMedio, label = "Aptidão Média")
    #ax.plot(range(len(hMax)), hMax, label = "Aptidão Máxima")
    #ax.set_xlabel("Gerações")  
    #ax.set_ylabel("Aptidão")
    #ax.legend()
    #matplotlib.pyplot.savefig("teste")
    return m, bestx, gen

#Executar uma vez
#lt = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
lt = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
taxaMutacao = input("Digite a taxa de mutacao: ")
taxaCross = input("Digite a taxa de Crossover: ")
maxGen = input("Digite o maximo de geracoes: ")
print(Genetico(lt, float(j), float(k), int(maxGen)))

# #Teste de variação de parâmetros
# taxaCross = [0.3, 0.6, 0.9]
# taxaMutacao = [0.02, 0.04, 0.08]
# Gen = []
# mediaGen = []
# for j in taxaCross:
#     for k in taxaMutacao:
#         for i in range(100):
#             m, bestx, gen = Genetico(lt, float(j), float(k), int(maxGen))
#             Gen.append(gen)
#             #print(m, bestx)
#         mediaGen.append(sum(Gen)/len(Gen))

# f = open("exp1.txt", "a")
# #f.write("x, " + str(bestx) + "\t")
# f.write("gen, " + str(mediaGen) + "\n")
# f.close()

import random
import math
import copy
import matplotlib.pyplot as plt
import matplotlib
import statistics as s

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

#calcula valor de x
def CalcX(lista):
    x = 0
    for j in range(len(lista)):
        x += lista[j]*math.pow(2,-j-1)
    return x

#Calculo da Aptidão
def Aptidao(m):
    apt = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(m)-1):
        x = CalcX(m[i])
        fx = CalcFunc(x)
        apt[i] = fx
    return apt
        
#calculo do valor de x na função        
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
    distaux += math.ceil(distMax*360/soma)
    dist1.append(distaux)
    for i in range(len(dist)):
        sorteio = random.randint(0, 360)
        for j in range(len(dist1)):
            if sorteio <= dist1[j]:
                pop.append(j)
                break
    return pop

#selecao por torneio
def Torneio(dist, distMax):
    pop = []
    dist.append(distMax)
    #print(dist)
    for i in range(len(dist)):
        sorteio = random.sample(range(len(dist)), 3)
        #print(sorteio)
        if dist[sorteio[0]] >= dist[sorteio[1]] and dist[sorteio[0]] >= dist[sorteio[2]]:
            pop.append(sorteio[0])
        elif dist[sorteio[1]] >= dist[sorteio[0]] and dist[sorteio[1]] >= dist[sorteio[2]]:
            pop.append(sorteio[1])
        elif dist[sorteio[2]] >= dist[sorteio[1]] and dist[sorteio[2]] >= dist[sorteio[0]]:
            pop.append(sorteio[2])
    return pop

#seleção por amostragem estocástica
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
    for i in range(len(dist)):
        for j in range(len(dist1)):
            if sorteio <= dist1[j]:
                pop.append(j)
                break
        sorteio += esp
        if sorteio > 360:
            sorteio -= 360
    return pop

#Realiza o Crossover
def Crossover(l, q):
    cp = random.randint(0, len(l)-1) #ponto de crossover
    for i in range(cp, len(l)):
        l[i], q[i] = q[i], l[i]
    return l, q

#realiza mutação
def Mutacao(pm, m):
    for i1,i in enumerate(m):
        for j in range(len(i)):
            if random.random() <= pm:
                #print("oi", i1, j)
                if i[j] == 0:
                    i[j] = 1
                else: 
                    i[j] = 0

#monta a matriz da nova população
def Reproducao(pop, m, pc):
    m1 = [] 
    #pc = 0.6 #taxa de crossover*
    crosspares = []
    for i in range(int(float(len(pop))/2)): #montando pares
        crosspares.append((pop[2*i], pop[2*i+1]))
    #print("CP:", crosspares) 
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

#algoritmo principal
def Genetico(pc, pm, maxGen, k):
    kaux = k #variável auxiliar ao critério de parada
    m = PopulacaoRandom() #gera uma populacao inicial aleatoria
    h = Aptidao(m) #calcula a distancia de Hamming da pop atual até a bitstring desejada (aptidao)
    besth = max(h) #salva melhor aptidão
    bestx = m[h.index(besth)] #salva melhor individuo
    m.append(bestx) #elitismo
    hMedio = []
    hMax = []
    hMedio.append((sum(h)+besth)/(len(h)+1)) #calcula aptidao media da geracao
    gen = 0
    while gen < maxGen and 1.0 not in h and k >= 0: #Condicao de Parada: Max de geracoes e aptidao e número de iterações em melhora
        #pop = Roleta(h, besth) #selecao por roleta #retorna os indices da nova populacao
        #pop = Torneio(h, besth)
        pop = SUS(h, besth)
        m[len(m)-1] = copy.deepcopy(bestx)
        m = Reproducao(pop, m, pc)
        Mutacao(pm, m)
        h = Aptidao(m)
        hMedio.append((sum(h)+besth)/(len(h)+1))
        gen += 1
        if besth < max(h):
            besth = max(h)
            bestx = m[h.index(besth)]
            k = kaux
        else: 
            k -= 1
        hMax.append(besth)
    # fig, ax = plt.subplots()
    # ax.plot(range(len(hMedio)), hMedio, label = "Aptidão Média")
    # ax.plot(range(len(hMax)), hMax, label = "Aptidão Máxima")
    # ax.set_xlabel("Gerações")  
    # ax.set_ylabel("Aptidão")
    # ax.legend()
    # matplotlib.pyplot.savefig("teste2")
    return m, bestx, gen

taxaMutacao = input("Digite a taxa de mutacao: ")
taxaCross = input("Digite a taxa de Crossover: ")
maxGen = input("Digite o maximo de geracoes: ")
maxk = input("Digite o numero max de iteracoes para convergencia: ")
print(Genetico(float(taxaCross), float(taxaMutacao), int(maxGen), int(maxk)))


#Teste de variação de parâmetros
# taxaCross = [0.3, 0.6, 0.9]
# taxaMutacao = [0.02, 0.04, 0.08]
# Gen = []
# mediaGen = []
# BestX = []
# mediaX  = []
# for j in taxaCross:
#     for k in taxaMutacao:
#         for i in range(100):
#             m, bestx, gen = Genetico(float(j), float(k), int(maxGen), int(maxk))
#             Gen.append(gen)
#             BestX.append(CalcX(bestx))
#             #print(m, bestx)
#         mediaGen.append(sum(Gen)/len(Gen))
#         mediaX.append(sum(BestX)/len(BestX))

# f = open("exp2.txt", "a")
# #f.write("x, " + str(bestx) + "\t")
# f.write("gen, " + str(mediaGen) + "\n")
# f.write("x" + str(mediaX) + "\n")
# f.close()

# Gen = []
# BestX = []
# for i in range(1000):
#     m, bestx, gen = Genetico(float(taxaCross), float(taxaMutacao), int(maxGen), int(maxk))
#     Gen.append(gen)
#     BestX.append(CalcX(bestx))

# f = open("exp21.txt", "a")
# f.write("Algoritmo Genético SUS \n")
# f.write("Mediagen, " + str(s.mean(Gen)) + "\n")
# f.write("STDgen, " + str(s.stdev(Gen)) + "\n")
# f.write("Mediangen, " + str(s.median(Gen)) + "\n")
# #f.write("Modegen, " + str(s.mode(Gen)) + "\n")

# f.write("MediaX, " + str(s.mean(BestX)) + "\n")
# f.write("STDX, " + str(s.stdev(BestX)) + "\n")
# f.write("MedianX, " + str(s.median(BestX)) + "\n\n")
# #f.write("ModeX, " + str(s.mode(Bestx)) + "\n\n")
# f.close()

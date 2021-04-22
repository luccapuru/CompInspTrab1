import random
import math
import copy
import matplotlib.pyplot as plt
import matplotlib
import statistics as s
def Escala(num):
    scale = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4
    }
    return scale.get(num, -1)

def CalcX(lista):
    x = 0
    k = 1
    for j in range(1,4)[::-1]:
        x += lista[k]*math.pow(2,j-1)
        k += 1
    x = Escala(x)
    for j in range(4, len(lista)):
        x += lista[j]*math.pow(2,-j+3)
    if lista[0] == 0:
        x *= -1
    return x

def GeraX(lista):
    x = -10
    while (x > 5 or x < -5):
        for j in range(len(lista)):
            lista[j] = random.randint(0,1)
        x = CalcX(lista)

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
    n = copy.deepcopy(m)
    for i in range(len(m)):
        GeraX(m[i])
    for i in range(len(n)):
        GeraX(n[i])
    return m,n

def Aptidao(m, n):
    apt = [0, 0, 0, 0, 0, 0, 0, 0]
    #x = 0
    for i in range(len(m)-1):
            x = CalcX(m[i])
            y = CalcX(n[i])
            f = CalcFunc(x,y)
            apt[i] = 1/(1+f)
        #x = 0
    return apt

def CalcFunc(x, y):
    return (1-x)**2 + 100*(y - x**2)**2

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
        for j in range(len(dist1)):
            if sorteio <= dist1[j]:
                pop.append(j)
                break
    return pop

def Torneio(dist, distMax):
    pop = []
    dist.append(distMax)
    for i in range(len(dist)):
        sorteio = random.sample(range(len(dist)), 3)
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
    for i in range(len(dist)):
        for j in range(len(dist1)):
            if sorteio <= dist1[j]:
                pop.append(j)
                break
        sorteio += esp
        if sorteio > 360:
            sorteio -= 360
    return pop

def Crossover(l, q, cp):
    for i in range(cp, len(l)):
        l[i], q[i] = q[i], l[i]
    return l, q

def Mutacao(pm, m):
    for i1,i in enumerate(m):
        for j in range(len(i)):
            if random.random() <= pm:
                #print("oi", i1, j)
                if i[j] == 0:
                    i[j] = 1
                else: 
                    i[j] = 0

def Reproducao(pop, m, n, pc):
    m1 = []
    n1 = [] 
    crosspares = []
    for i in range(int(float(len(pop))/2)): #montando pares
        crosspares.append((pop[2*i], pop[2*i+1]))
    for i in range(len(crosspares)):
        if(random.random() <= pc):
            cp = random.randint(0, len(m[0])-1) #ponto de crossover
            maux = copy.deepcopy(m)
            naux = copy.deepcopy(n)
            maux[crosspares[i][0]], maux[crosspares[i][1]] = Crossover(maux[crosspares[i][0]], maux[crosspares[i][1]], cp)
            naux[crosspares[i][0]], naux[crosspares[i][1]] = Crossover(naux[crosspares[i][0]], naux[crosspares[i][1]], cp)
            m1.append(copy.deepcopy(maux[crosspares[i][0]]))
            m1.append(copy.deepcopy(maux[crosspares[i][1]]))
            n1.append(copy.deepcopy(naux[crosspares[i][0]]))
            n1.append(copy.deepcopy(naux[crosspares[i][1]]))
        else:
            m1.append(copy.deepcopy(m[crosspares[i][0]]))
            m1.append(copy.deepcopy(m[crosspares[i][1]]))
            n1.append(copy.deepcopy(n[crosspares[i][0]]))
            n1.append(copy.deepcopy(n[crosspares[i][1]]))
    m1.append(copy.deepcopy(m[len(m)-1]))
    n1.append(copy.deepcopy(n[len(n)-1]))
    return m1, n1

def Genetico(pc, pm, maxGen, k):
    kaux = k
    m, n = PopulacaoRandom() #gera uma populacao inicial aleatoria
    h = Aptidao(m, n) #calcula a distancia de Hamming da pop atual até a bitstring desejada (aptidao)
    besth = max(h)
    bestx = m[h.index(besth)]
    m.append(bestx)
    besty = n[h.index(besth)]
    n.append(besty)
    hMedio = []
    hMax = []
    hMedio.append((sum(h)+besth)/(len(h)+1)) #calcula aptidao media da geracao
    gen = 0
    while gen < maxGen and 1.0 not in h and k >= 0: #Condicao de Parada: Max de geracoes e aptidao 
        #pop = Roleta(h, besth) #selecao por roleta #retorna os indices da nova populacao
        #pop = Torneio(h, besth)
        pop = SUS(h, besth)
        m[len(m)-1] = copy.deepcopy(bestx)
        n[len(n)-1] = copy.deepcopy(besty)
        m, n = Reproducao(pop, m, n, pc)
        Mutacao(pm, m)
        Mutacao(pm, n)
        h = Aptidao(m, n)
        hMedio.append((sum(h)+besth)/(len(h)+1))
        gen += 1
        if besth < max(h):
            besth = max(h)
            bestx = m[h.index(besth)]
            besty = n[h.index(besth)]
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
    # matplotlib.pyplot.savefig("teste3")
    return bestx, besty, gen

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
# BestY = []
# mediaY = []
# for j in taxaCross:
#     for k in taxaMutacao:
#         for i in range(100):
#             bestx, besty, gen = Genetico(float(j), float(k), int(maxGen), int(maxk))
#             Gen.append(gen)
#             BestX.append(CalcX(bestx))
#             BestY.append(CalcX(besty))
#         mediaGen.append(sum(Gen)/len(Gen))
#         mediaX.append(sum(BestX)/len(BestX))
#         mediaY.append(sum(BestY)/len(BestY))

# f = open("exp3.txt", "a")
# #f.write("x, " + str(bestx) + "\t")
# f.write("gen, " + str(mediaGen) + "\n")
# f.write("x" + str(mediaX) + "\n")
# f.write("y" + str(mediaY) + "\n")
# f.close()

# Gen = []
# BestX = []
# BestY = []
# for i in range(1000):
#     bestx, besty, gen = Genetico(float(taxaCross), float(taxaMutacao), int(maxGen), int(maxk))
#     Gen.append(gen)
#     BestX.append(CalcX(bestx))
#     BestY.append(CalcX(besty))

# f = open("exp31.txt", "a")
# f.write("Algoritmo Genético SUS \n")
# f.write("Mediagen, " + str(s.mean(Gen)) + "\n")
# f.write("STDgen, " + str(s.stdev(Gen)) + "\n")
# f.write("Mediangen, " + str(s.median(Gen)) + "\n")
# #f.write("Modegen, " + str(s.mode(Gen)) + "\n")

# f.write("MediaX, " + str(s.mean(BestX)) + "\n")
# f.write("STDX, " + str(s.stdev(BestX)) + "\n")
# f.write("MedianX, " + str(s.median(BestX)) + "\n")
# #f.write("ModeX, " + str(s.mode(Bestx)) + "\n\n")

# f.write("MediaY, " + str(s.mean(BestY)) + "\n")
# f.write("STDY, " + str(s.stdev(BestY)) + "\n")
# f.write("MedianY, " + str(s.median(BestY)) + "\n\n")
# #f.write("ModeX, " + str(s.mode(Bestx)) + "\n\n")
# f.close()

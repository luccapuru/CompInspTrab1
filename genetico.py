import random
import math
import copy

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
    for i,lista in enumerate(m):
        for j,num in enumerate(lista):
            if m[i][j] != l[j]:
                dist[i] += 1
    return dist

#selecao por roleta
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
    #print(dist1)
    for i in range(len(dist)):
        sorteio = random.randint(0, 360)
        #print(sorteio)
        for j in range(len(dist)):
            if sorteio < dist1[j]:
                pop.append(j)
                break
    print("Pop", pop)
    #for i in range(len(m)):
        #m[i] = m[pop[i]]
    #print("M mod:", m)
    return pop

#def AtualizaPop(pop, m):
    #m1 = [] 
    #for i in range(len(m)):
        #m1.append(copy.deepcopy(m[pop[i]]))
    #return m1

def Crossover(l, q):
    cp = random.randint(0, len(l)-1) #ponto de crossover
    print(l)
    print(q)
    print("Ponto de crossover:", cp)
    for i in range(cp, len(l)):
        l[i], q[i] = q[i], l[i]
    print(l)
    print(q, "\n\n")
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


def Reproducao(pop, m):
    m1 = [] 
    pc = 0.6 #taxa de crossover
    crosspares = []
    for i in range(int(float(len(pop))/2)): #montando pares
        crosspares.append((pop[2*i], pop[2*i+1]))
    print("CP:", crosspares) 
    for i in range(len(crosspares)):
        if(random.random() <= pc):
            #m1[crosspares[i][0]], m1[crosspares[i][1]] = Crossover(m[crosspares[i][0]], m[crosspares[i][1]])
            print("Cross", i)
            maux = copy.deepcopy(m)
            maux[crosspares[i][0]], maux[crosspares[i][1]] = Crossover(maux[crosspares[i][0]], maux[crosspares[i][1]])
            m1.append(copy.deepcopy(maux[crosspares[i][0]]))
            m1.append(copy.deepcopy(maux[crosspares[i][1]]))
        else:
            print("NCross", i)
            m1.append(copy.deepcopy(m[crosspares[i][0]]))
            print(crosspares[i][0], m[crosspares[i][0]])
            m1.append(copy.deepcopy(m[crosspares[i][1]]))
            print(crosspares[i][1], m[crosspares[i][1]], "\n\n")
    print("M::", m)
    return m1

def Genetico(bitstring, pc, pm, maxGen):
    m = PopulacaoRandom() #gera uma populacao inicial aleatoria
    h = Distancia(m, bitstring) #calcula a distancia de Hamming da pop atual até a bitstring desejada (aptidao)
    hMedio = []
    hMedio.append(sum(h)/len(h)) #calcula aptidao media da geracao
    gen = 0
    print("h:", h)
    print("hMedio:", hMedio)
    print("Gen:", gen)
    while gen <= maxGen and 12 not in h: #Condicao de Parada: Max de geracoes e aptidao 
        pop = Roleta(h) #selecao por roleta #retorna os indices da nova populacao
        m = Reproducao(pop, m)
        Mutacao(0.02, m)
        h = Distancia(m, bitstring)
        hMedio.append(sum(h)/len(h))
        gen += 1
        print("h:", h)
        print("hMedio:", hMedio)
        print("Gen:", gen)
    return m 

#lt = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
lt = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
taxaMutacao = input("Digite a taxa de mutacao: ")
taxaCross = input("Digite a taxa de Crossover: ")
maxGen = input("Digite o maximo de geracoes: ")
print(Genetico(lt, float(taxaCross), float(taxaMutacao), int(maxGen)))

#matriz = PopulacaoRandom()
#print("M:", matriz)
#lt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #bitstring desejada (invertida)
#d = Distancia(matriz, lt)
#print("D", d)
#pop = Roleta(d)
#print(Roleta(d))
# = AtualizaPop(pop, matriz)
#print("M:", matriz)
#matriz1 = Reproducao(pop, matriz)
#print("M':", matriz1)
#Mutacao(0.02, matriz1)
#print("M:", matriz)
#print("M'':", matriz1)


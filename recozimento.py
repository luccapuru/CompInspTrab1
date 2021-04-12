import random
import math

def SolucaoRandom():
    solucao = random.random()
    return solucao

def CalcFunc(x):
    result = 2**(-2*((x-0.1)/0.9)**2) * (math.sin(5*math.pi*x))**6
    return result

#print(CalcFunc(solucaoRandom))

def Perturb(x, mu, sigma):
    return x + random.gauss(mu, sigma)

def TrocarTemp(T, b):
    T1 = T*b
    return T

def Recozimento(maxI, mu, sigma, k):
    T = 10
    kaux = k
    #inicializar x
    x = SolucaoRandom()
    #avaliar x
    resulx = CalcFunc(x)
    #inicializar melhor ponto encontrado ate o momento
    bestx = x 
    bestresul = resulx
    print("x inicial:", x)
    i = 0
    while i < maxI and k >= 0:
        x1 = Perturb(x, mu, sigma)
        print("x1 Encontrado:", x1)
        resulx = CalcFunc(x)
        resulx1 = CalcFunc(x1)
        if resulx1 > bestresul:
            bestx = x1
            bestresul = resulx1
        prob = random.random()
        if prob < math.exp((resulx1 - resulx)/T): 
            x = x1
            k = kaux
            print("troca")
        else:
            k -= 1
        i = i + 1
        T = TrocarTemp(T, 0.7)
        if T <= 1:
            T = 10
        #print("Prob:", prob)
        print("x Atual:", x)
        print("K:", k)
    print("Numero de iteracoes:", i)
    return bestx

maxI = input("Digite o valor máximo de iteracoes: ")
mu = input("Digite o valor de mu: ")
sigma = input("Digite o valor de sigma: ")
k = input("Digite o valor de iteracoes do criterio de convergencia: ")
solucao = Recozimento(int(maxI), float(mu), float(sigma), int(k))
#print("Numero de iteracoes:", i)
print("Solucao Encontrada:",solucao)
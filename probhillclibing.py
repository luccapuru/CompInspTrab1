import random
import math

def SolucaoRandom():
    solucao = random.random()
    return solucao

def CalcFunc(x):
    result = 2**(-2*((x-0.1)/0.9)**2) * (math.sin(5*math.pi*x))**6
    return result

#print(CalcFunc(solucaoRandom))

def perturb(x, mu, sigma):
    return x + random.gauss(mu, sigma)

def SubindoColina(maxI, mu, sigma, k, g):
    kaux = k
    T = 1
    #Inicializar x
    x = SolucaoRandom()
    #Avaliar x
    resulx = CalcFunc(x)
    print("x inicial:", x)
    i = 1
    while i < maxI and k >= 0 and resulx != g:
        x1 = perturb(x, mu, sigma)
        print("x1 Encontrado:", x1)
        resulx = CalcFunc(x)
        resulx1 = CalcFunc(x1)
        #prob = random.random()
        if random.random() < (1/(1+math.exp((resulx - resulx1)/T))): 
            x = x1
            print("troca")
            k = kaux
        else:
            k -= 1
        i = i + 1
        print("x Atual:", x)
        print("K:", k)
    print("Numero de iteracoes:", i)
    return x

maxI = input("Digite o valor máximo de iteracoes: ")
mu = input("Digite o valor de mu: ")
sigma = input("Digite o valor de sigma: ")
k = input("Digite o valor de iteracoes do criterio de convergencia: ")
g = input("Valor maximo da funcao: ")
solucao = SubindoColina(int(maxI), float(mu), float(sigma), int(k), float(g))
print("Solucao Encontrada:",solucao)
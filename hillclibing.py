import random
import math

#Gera uma uma solucao aletoria para inicializar x
def SolucaoRandom():
    solucao = random.random()
    return solucao

#Calcula o valor da funcao em x
def CalcFunc(x):
    result = 2**(-2*((x-0.1)/0.9)**2) * (math.sin(5*math.pi*x))**6
    return result

#Perturba x utilizando um ruído gaussiano
def perturb(x, mu, sigma):
    return x + random.gauss(mu, sigma)

#Algoritmo
def SubindoColina(maxI, mu, sigma, k, g):
    kaux = k
    #Inicializar x
    x = SolucaoRandom()
    resulx = CalcFunc(x)
    print("x inicial:", x)    
    i = 1
    #Criterio de parada: numero maximo de iteracoes, x nao mudou nas ultimas k iteracoes
    while i < maxI and k >= 0 and resulx != g:
        x1 = perturb(x, mu, sigma)
        print("x1 Encontrado:", x1)
        #Avaliar x atual e o x1 candidato
        resulx = CalcFunc(x)
        resulx1 = CalcFunc(x1)
        if resulx1 > resulx:
            x = x1
            k = kaux
        else:
            k -= 1
        i = i + 1
        print("x Atual:", x)
        print("K:", k)
    return x

maxI = input("Digite o valor máximo de iteracoes: ")
mu = input("Digite o valor de mu: ")
sigma = input("Digite o valor de sigma: ")
k = input("Digite o valor de iteracoes do criterio de convergencia: ")
g = input("Valor maximo da funcao: ")
solucao = SubindoColina(int(maxI), float(mu), float(sigma), int(k), float(g))
print("Solucao Encontrada:",solucao)
import random
import math
import statistics as s

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

#Algoritmo principal
def SubindoColina(maxI, mu, sigma, k, g):
    kaux = k #variável auxiliar ao critério de parada
    #Inicializar x
    x = SolucaoRandom()
    #Avaliar x
    resulx = CalcFunc(x)  
    i = 0
    #Criterio de parada: numero maximo de iteracoes, x nao mudou nas ultimas k iteracoes e achou o ponto de maximo
    while i < maxI and k >= 0 and resulx != g:
        #Pertuba x
        x1 = perturb(x, mu, sigma)
        #Avaliar x atual e o x1 candidato
        resulx = CalcFunc(x)
        resulx1 = CalcFunc(x1)
        if resulx1 > resulx: # se x novo for maior substitui e reseta o critério de parada
            x = x1
            k = kaux
        else:
            k -= 1 # decrementa o critério de parada
        i = i + 1
    return x, i

#entrada do usuário
maxI = input("Digite o valor máximo de iteracoes: ")
mu = input("Digite o valor de mu: ")
sigma = input("Digite o valor de sigma: ")
k = input("Digite o valor de iteracoes do criterio de convergencia: ")
g = input("Valor maximo da funcao: ")
print(SubindoColina(int(maxI), float(mu), float(sigma), int(k), float(g)))

# #Teste 1000 vezes
# Gen = []
# BestX = []
# for i in range(1000):
#     solucao, gen = SubindoColina(int(maxI), float(mu), float(sigma), int(k), float(g))
#     Gen.append(gen)
#     BestX.append(solucao)

# #saída do algoritmo salva em arquivo
# f = open("exp21.txt", "a")
# f.write("HillClinbing \n")
# f.write("Mediagen, " + str(s.mean(Gen)) + "\n")
# f.write("STDgen, " + str(s.stdev(Gen)) + "\n")
# f.write("Mediangen, " + str(s.median(Gen)) + "\n")
# #f.write("Modegen, " + str(s.mode(Gen)) + "\n")

# f.write("MediaX, " + str(s.mean(BestX)) + "\n")
# f.write("STDX, " + str(s.stdev(BestX)) + "\n")
# f.write("MedianX, " + str(s.median(BestX)) + "\n")
# #f.write("ModeX, " + str(s.mode(Bestx)) + "\n\n")
# f.close()


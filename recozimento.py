import random
import math
import statistics as s

#gera solução inical aleatória
def SolucaoRandom():
    solucao = random.random()
    return solucao

#calcula valor de x na função
def CalcFunc(x):
    result = 2**(-2*((x-0.1)/0.9)**2) * (math.sin(5*math.pi*x))**6
    return result

#pertuba x com ruído gaussiano
def Perturb(x, mu, sigma):
    return x + random.gauss(mu, sigma)

#troca a temperatura
def TrocarTemp(T, b):
    T1 = T*b
    return T

def Recozimento(maxI, mu, sigma, k):
    T = 10 #iniciar tempeatura
    kaux = k #variável auxiliar ao critério de parada
    #inicializar x
    x = SolucaoRandom()
    #avaliar x
    resulx = CalcFunc(x)
    #inicializar melhor ponto encontrado ate o momento
    bestx = x 
    bestresul = resulx
    i = 0
    #Critério de Parada: Máximo de iterações ou número de iterações sem mudar o x
    while i < maxI and k >= 0:
        #perturbar x
        x1 = Perturb(x, mu, sigma)
        #avaliar x atual e antigo
        resulx = CalcFunc(x)
        resulx1 = CalcFunc(x1)
        if resulx1 > bestresul: #troca melhor x 
            bestx = x1
            bestresul = resulx1
        prob = random.random()
        if prob < math.exp((resulx1 - resulx)/T): #troca baseado na temperatura o x atual e reseta critério de parada
            x = x1
            k = kaux
        else:
            k -= 1 #decrementa critério de parada
        i = i + 1
        T = TrocarTemp(T, 0.7) #diminui temperatura geometricamente
        if T <= 1: #reseta a temperatura se ficar muito baixa
            T = 10
    return bestx, i

#entrada do usuário
maxI = input("Digite o valor máximo de iteracoes: ")
mu = input("Digite o valor de mu: ")
sigma = input("Digite o valor de sigma: ")
k = input("Digite o valor de iteracoes do criterio de convergencia: ")
print(Recozimento(int(maxI), float(mu), float(sigma), int(k)))

#teste 1000 vezes
# Gen = []
# BestX = []
# for i in range(1000):
#     solucao, gen = Recozimento(int(maxI), float(mu), float(sigma), int(k))
#     Gen.append(gen)
#     BestX.append(solucao)

#saida do algoritmo em um arquivo
# f = open("exp21.txt", "a")
# f.write("Recozimento Simulado \n")
# f.write("Mediagen, " + str(s.mean(Gen)) + "\n")
# f.write("STDgen, " + str(s.stdev(Gen)) + "\n")
# f.write("Mediangen, " + str(s.median(Gen)) + "\n")
# #f.write("Modegen, " + str(s.mode(Gen)) + "\n")

# f.write("MediaX, " + str(s.mean(BestX)) + "\n")
# f.write("STDX, " + str(s.stdev(BestX)) + "\n")
# f.write("MedianX, " + str(s.median(BestX)) + "\n\n")
# #f.write("ModeX, " + str(s.mode(Bestx)) + "\n\n")
# f.close()
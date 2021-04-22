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

def SubindoColina(maxI, mu, sigma, k, g):
    kaux = k #variável auxiliar ao critério de parada
    T = 1 #iniciar T
    #Inicializar x
    x = SolucaoRandom()
    #Avaliar x
    resulx = CalcFunc(x)
    i = 0
    #Criterio de parada: numero maximo de iteracoes, x nao mudou nas ultimas k iteracoes e achou o ponto de maximo
    while i < maxI and k >= 0 and resulx != g:
        x1 = perturb(x, mu, sigma) #perturba x
        #Avaliar x atual e o x1 candidato
        resulx = CalcFunc(x)
        resulx1 = CalcFunc(x1)
        #prob = random.random()
        if random.random() < (1/(1+math.exp((resulx - resulx1)/T))): #verifica se troca o x
            x = x1
            k = kaux #reseta critério de parada
        else:
            k -= 1 #incrementa critério de parada
        i = i + 1
    return x, i

#entrada do usuário
maxI = input("Digite o valor máximo de iteracoes: ")
mu = input("Digite o valor de mu: ")
sigma = input("Digite o valor de sigma: ")
k = input("Digite o valor de iteracoes do criterio de convergencia: ")
g = input("Valor maximo da funcao: ")
solucao = SubindoColina(int(maxI), float(mu), float(sigma), int(k), float(g))
print("Solucao Encontrada:",solucao)

# #Teste 1000 vezes
# Gen = []
# BestX = []
# for i in range(1000):
#     solucao, gen = SubindoColina(int(maxI), float(mu), float(sigma), int(k), float(g))
#     Gen.append(gen)
#     BestX.append(solucao)

# #salvar resultado em arquivo
# f = open("exp21.txt", "a")
# f.write("ProbHillClinbing \n")
# f.write("Mediagen, " + str(s.mean(Gen)) + "\n")
# f.write("STDgen, " + str(s.stdev(Gen)) + "\n")
# f.write("Mediangen, " + str(s.median(Gen)) + "\n")
# #f.write("Modegen, " + str(s.mode(Gen)) + "\n")

# f.write("MediaX, " + str(s.mean(BestX)) + "\n")
# f.write("STDX, " + str(s.stdev(BestX)) + "\n")
# f.write("MedianX, " + str(s.median(BestX)) + "\n")
# #f.write("ModeX, " + str(s.mode(Bestx)) + "\n\n")
# f.close()
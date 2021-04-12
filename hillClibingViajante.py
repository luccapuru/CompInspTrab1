import random
caixeiro = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0]
]

def SolucaoRandom(caixeiro):
    cidades = list(range(len(caixeiro)))
    print(cidades)
    solucao = []

    for i in range(len(caixeiro)):
        cidadeRandom = cidades[random.randint(0, len(cidades) - 1)]
        solucao.append(cidadeRandom)
        cidades.remove(cidadeRandom)

    return solucao

solucaoRandom = SolucaoRandom(caixeiro)
print(solucaoRandom)

def TamanhoRota(caixeiro, solucao):
    tamanhoRota = 0
    for i in range(len(solucao)):
        print("i-1:",solucao[-2])
        print("i:",solucao[i])
        tamanhoRota += caixeiro[solucao[i - 1]][solucao[i]]
    return tamanhoRota

print(TamanhoRota(caixeiro, solucaoRandom))
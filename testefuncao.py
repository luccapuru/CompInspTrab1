import math
strx = input("Digite o valor de x: ")
x = float(strx)
g = 2**(-2*((x-0.1)/0.9)**2) * (math.sin(5*math.pi*x))**6
print("Valor de g é:", g)
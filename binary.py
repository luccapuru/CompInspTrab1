import math
import random

def CalcFunc(x):
    result = 2**(-2*((x-0.1)/0.9)**2) * (math.sin(5*math.pi*x))**6
    return result
m = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1]
]
for i,lista in enumerate(m):
        for j,num in enumerate(lista):
            m[i][j] = random.randint(0,1)
apt = []
x = 0
for i in range(len(m)):
    for j in range(len(m)):
        x += m[i][j]*math.pow(2,-j-1)
    fx = CalcFunc(x)
    apt.append(fx)
    x = 0
print(m)
print(apt)
besth = max(apt)
bestx = m[apt.index(besth)]
print("BH:", besth)
print("BX:", bestx)

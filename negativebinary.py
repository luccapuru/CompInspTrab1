import math
import random
import copy
#def CalcFunc(x):
    #result = 2**(-2*((x-0.1)/0.9)**2) * (math.sin(5*math.pi*x))**6
    #return result
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
n = copy.deepcopy(m)
#m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#for i,lista in enumerate(m):

    #m[j] = 1

def Escala(num):
    scale ={
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4
    }
    return scale.get(num, -1)

def CalcX(lista):
    x = 0
    k = 1
    for j in range(1,4)[::-1]:
        #print(j)
        x += lista[k]*math.pow(2,j-1)
        k += 1
    x = Escala(x)
    for j in range(4, len(lista)):
        x += lista[j]*math.pow(2,-j+3)
    if lista[0] == 0:
        x *= -1
    return x

def GeraX(lista):
    x = -10
    while (x > 5 or x < -5):
        for j in range(len(lista)):
            lista[j] = random.randint(0,1)
        x = CalcX(lista)
        print(lista, x)

def CalcFunc(x, y):
    return (1-x)**2 + 100*(y - x**2)**2

def Aptidao(m, n):
    apt = []
    #x = 0
    for i in range(len(m)):
        x = CalcX(m[i])
        y = CalcX(n[i])
        f = CalcFunc(x,y)
        apt.append(1/(1+f))
    #x = 0
    return apt

print("x")
for i in range(len(m)):
    GeraX(m[i])
print("y")
for i in range(len(m)):
    GeraX(n[i])

print("x:", CalcX([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

print(m)
print(n)
print(CalcFunc(1,1))
print(Aptidao(m,n))
#b = input("..:")
#Escala(int(b))


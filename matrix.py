m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

l = [0, 1, 2, 3, 4, 5, 6, 7]

m1 = [] 
for i in range(len(m)):
    m1.append(m[l[i]])


print(m1)

for i in range(4):
    print("Pares:", l[2*i], l[2*i+1])

x, y = 1, 3

print(x, y)
import copy

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, 24]
]

l = [2, 2, 0, 3, 5, 4, 6, 1]

m1 = [] 
for i in range(len(m)):
    m1.append(copy.deepcopy(m[l[i]]))


print(m1)

m1[0][1] = 100

print(m1)

#x = []
#for i in range(4):
 #   x.append((l[2*i], l[2*i+1]))

#print(x)
#print(m[x[1][1]])

#for i in range(len(x)):
 #   print(x[i][0], m[x[i][0]])
  #  print(x[i][1], m[x[i][1]])

#x, y = 1, 3

#print(x, y)
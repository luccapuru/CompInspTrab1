import copy
a=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, 24]
]
b = copy.deepcopy(a)
b.append([25, 26, 27])
print("a", a)
print("b", b)
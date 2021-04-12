import random
import math

rand = random.random()
i = 0
while i < 10:
    x = random.random()
    y = 1/(1+math.exp((random.random() - random.random())/10))
    if x > y:
        print("Yes")
    else:
        print("No")
    i += 1
# library to generate a random number
import random

# function for implementing the single-point crossover
def crossover(l, q):
	print("l", l)
	print("q", q)
# converting the string to list for performing the crossover
	#l = list(l)
	#q = list(q)

# generating the random number to perform crossover
	k = random.randint(0, len(l)-1)
	print("Crossover point :", k)
	#x = range(int(float(len(l))/2))
	#for i in range(int(float(len(l))/2)):
		#print("Teste")

# interchanging the genes
	for i in range(k, len(l)):
		l[i], q[i] = q[i], l[i]
	#l = ''.join(l)
	#q = ''.join(q)
	print(l)
	print(q, "\n\n")
	return l, q


# patent chromosomes:

s = [
    [1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0]
]
print("Parents")
print("P1 :", s[0])
print("P2 :", s[1], "\n")

# function calling and storing the off springs for
# next generation crossover
for i in range(5):
	print("Generation ", i+1, "Childrens :")
	s[0], s[1] = crossover(s[0], s[1])

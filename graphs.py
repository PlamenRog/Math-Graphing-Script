# Plotting and numbers
import matplotlib.pyplot as plt
import numpy as np

funcNum = int(input("How many functions would you like to plot: "))

funcArr = [] 

a = 0
while a <= funcNum-1:
	funcAlg = input("Enter function " + str(a+1) + ": ")
	funcArr.append(funcAlg)
	a+=1

# Labels and marks
x = np.linspace(-100, 100, 100)

#plt.title("Graph of the " + str(funcNum) + " functions.")
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(color = 'black')
plt.axvline(color = 'black')


# Function for graphing
def f(alg):
	fn = eval(alg)
	return fn


# Iterating through the array
for i in range(funcNum):
	n = funcArr[i]
	plt.plot(x, f(n))

plt.plot(x, f(funcAlg))
plt.show()
# Plotting and numbers
import matplotlib.pyplot as plt
import numpy as np


funcNum = int(input("How many functions would you like to plot: "))

funcArr = []
typeArr = []
colorArr = []
funcDraw = []

for a in range(funcNum):
    # Enters functions
    funcAlg = input("Enter function " + str(a+1) + ": ")
    funcArr.append(funcAlg)

    # Enters function type
    funcType = input("Enter function " + str(a+1) + "'s type(variable/variables): ")
    typeArr.append(funcType)

    # Enters function color
    funcCol = input("Enter function " + str(a+1) + "'s color(black, green, blue, yellow, cyan, gray): ")
    colorArr.append(funcCol)

# Labels and marks
x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)


#plt.title("Graph of the " + str(funcNum) + " functions.")
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(color = 'black')
plt.axvline(color = 'black')


# Function for graphing - single variable
def f(alg):
	fn = eval(alg)
	return fn

# Function for graphing - 2 variables
def g(y, alg):
	fn = eval(alg)
	return fn

# Iterating through the array
for i in range(funcNum):
    n = funcArr[i]

    if typeArr[i] == "variable" or typeArr[i] == "var":
        plt.plot(x, f(n), colorArr[i])

    elif typeArr[i] == "variables" or typeArr[i] == "vars":
        plt.plot(x, g(y, n), colorArr[i])





plt.show()

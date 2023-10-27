from calculos import pontos
import matplotlib.pyplot as plt
import numpy as np
import math

print("1 - sen(x)")
print("2 - cosx)")
print("3 - x*e^(-2x)")
eq = int(input("# Digite a equação desejada: "))

P = pontos(eq, False)
Px = P["Px"]
Py = P["Py"]
Py_5 = Py["5"]
Py_10 = Py["10"]
Py_30 = Py["30"]
orgN = [None, "sen(x)", "cos(x)", "x * e^-2x"]
org = [None, np.sin(Px), np.cos(Px), np.multiply(Px, np.float_power(math.e, (np.multiply(-2, Px))))]

plt.plot(Px, Py_5, label = "n = 5", linestyle = " ", marker = 'v') 
plt.plot(Px, Py_10, label = "n = 10", linestyle = " ", marker = '^') 
plt.plot(Px, Py_30, label = "n = 30", linestyle = " ", marker = '<') 
plt.plot(Px, org[eq], label = "sen(x)", linestyle=" ", marker = '>')
plt.show()
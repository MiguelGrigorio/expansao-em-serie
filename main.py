from calculos import pontos
import matplotlib.pyplot as plt
import numpy as np
import math

np.seterr(divide='ignore', invalid='ignore')

orgN =  [
            None,
            "sen(x)",
            "cos(x)",
            "x * e^-2x",
            "(1 + u)^-2",
            "(1 - u)^-2",
            "(1 + u)^-2 - (1 - u)^-2",
            "(1 - u)^-2 + (1 + u)^-2 - 2(1^-2)"
        ]

for i in range(1, len(orgN)):
    print(f"{i} - {orgN[i]}")

eq = int(input("# Digite a equação desejada: "))

if eq > 3:
    d = float(input("# Digite o tamanho de d: "))
else:
    d = 0

P = pontos(eq, False, d)
Px = P["Px"]
PPx = []
if eq > 3 and eq < 7:
    PPx = np.divide(d, np.multiply(2, Px))
elif eq == 7:
    PPx = np.divide(d, Px)
Py = P["Py"]
Py_5 = Py["5"]
Py_10 = Py["10"]
Py_30 = Py["30"]

# Diminuir quantidade de pontos
for _ in range(0):
    del Px[0]
    del Py_5[0]
    del Py_10[0]
    del Py_30[0]
org =   [
            None,
            np.sin(Px),
            np.cos(Px),
            np.multiply(Px, np.float_power(math.e, (np.multiply(-2, Px)))),
            np.power(np.add(1, Px), -2),
            np.power(np.subtract(1, Px), -2),
            np.subtract(np.power(np.add(1, PPx), -2),
                        np.power(np.subtract(1, PPx), -2)
                        ),
            np.subtract(np.add(
                               np.power(np.add(1, PPx), -2), np.power(np.subtract(1, PPx), -2)),
                               2
                       )
        ]

plt.plot(Px, Py_5, label = "n = 5", linestyle = " ", marker = 'v') 
plt.plot(Px, Py_10, label = "n = 10", linestyle = " ", marker = '^') 
plt.plot(Px, Py_30, label = "n = 30", linestyle = " ", marker = '<') 
plt.plot(Px, org[eq], label = orgN[eq], linestyle=" ", marker = '>')
plt.legend()
plt.show()

from functions import pontos
import matplotlib.pyplot as plt

funcLegend = {
                    "dipolo": "(1 + u)^-2 - (1 - u)^-2",
                    "quadrupolo": "(1 - u)^-2 + (1 + u)^-2 - 2(1^-2)"
             }

eq = input("# Digite a equação desejada: ")
Points = pontos(equacao = eq, data = False)

Px = Points["Px"]
Py = Points["Py"]
Py_5 = Py["5"]
Py_10 = Py["10"]
Py_30 = Py["30"]
Py_Original = Py["original"]

# Diminuir quantidade de pontos (melhora a curva)
for _ in range(1):
    del Px[-1]
    del Py_5[-1]
    del Py_10[-1]
    del Py_30[-1]
    del Py_Original[-1]

plt.plot(Px, Py_5, label = "n = 5", linestyle = " ", marker = 'v') 
plt.plot(Px, Py_10, label = "n = 10", linestyle = " ", marker = '^') 
plt.plot(Px, Py_30, label = "n = 30", linestyle = " ", marker = '<') 
plt.plot(Px, Py_Original, label = funcLegend[eq], linestyle = " ", marker = '>')
plt.gca().invert_xaxis() # Começa com u = 1, representando que o y é igual a distância do polo
plt.legend()
plt.show()

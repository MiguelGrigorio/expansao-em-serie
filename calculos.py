from sympy import factorial, diff, exp, Symbol
from math import pi

N = [5, 10, 30]


def dominio(equacao: int):

  def gerar_pontos(incremento: float):
    v = 0
    arr = []
    for _ in range(20):
      arr.append(v)
      v += incremento
    return arr

  if equacao < 3:
    return gerar_pontos(2 * float(pi) / 20)
  else:
    return gerar_pontos(4 / 20)


def somatorio(equacao: int, N: int, dominio: list):
  value = []
  for x in dominio:
    eq = 0
    for n in range(N + 1):
      match equacao:
        case 1:
          eq += ((-1)**n) * (x**((2 * n) + 1)) / factorial((2 * n) + 1)
        case 2:
          eq += ((-1)**n) * x**(2 * n) / factorial(2 * n)
        case 3:
          y = Symbol('y')
          eq += (diff(y * exp(-2 * y), y, n).subs(y, 0) * (y)**n) / factorial(n)
          eq = eq.subs(y, x)
          pass
        case _:
          raise Exception("Equação Inválida")
    value.append(eq)
  return value

def pontos(equacao: int, data: bool):

  dicio = {
    "Px": [],
    "Py": {
      "5": [],
      "10": [],
      "30": [],
    }
  }
  dom = dominio(equacao)
  dicio["Px"] = dom
  for vezes in N:
    eq = somatorio(equacao, vezes, dom)
    dicio["Py"][str(vezes)] = eq
  if data == True:
    with open('data.dat', 'w') as dat:
      for i in dicio["Py"].keys():
        for j in range(20):
          dat.write(f'{dicio["Px"][j]}\t{dicio["Py"][i][j]}\n')
        dat.write('\n')
  return dicio
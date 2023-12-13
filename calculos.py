from sympy import factorial, diff, exp, Symbol
from math import pi

N = [5, 10, 30]
d = 0

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
  elif equacao == 3:
    return gerar_pontos(4 / 20)
  else:
    v = d
    arr = []
    for _ in range(20):
      if equacao == 6:
        v = d/(2*v)
      else:
        v = d/v
      arr.append(v)
      v += 1/20
    return arr

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
          eq += (diff(y * exp(-2 * y), y, n).subs(y, 0) * y**n) / factorial(n)
          eq = eq.subs(y, x)
          pass
        case 4:
          u = Symbol('u')
          f = u ** (n + 1)
          eq += (diff(f, u) * (-1) ** n)
          eq = eq.subs(u, x)
        case 5:
          u = Symbol('u')
          g = u ** (n + 1)
          eq += diff(g, u)
          eq = eq.subs(u, x)
        case 6:
          u = Symbol('u')
          
          #f = 1/(2*y) ** (n + 1)
          f = u ** (n + 1)
          g = f
          eq += (diff(f, u) * (-1)**n) - diff(g, u)
          eq = eq.subs(u, x)
        case 7:
          u = Symbol('u')
          f = u ** (n + 1)
          g = f
          eq += (diff(f, u) * ((-1) ** n) + diff(g, u))
          if n == 0:
            eq += - (2 * diff(1 ** -2, u, n).subs(u, 0))
          eq = eq.subs(u, x)
        case _:
          raise Exception("Equação Inválida")
    value.append(eq)
  return value


def pontos(equacao: int, data: bool, distance: float):
  global d
  d = distance

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

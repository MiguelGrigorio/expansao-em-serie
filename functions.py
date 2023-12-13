from sympy import diff, Symbol

N = [5, 10, 30, "original"] # Número de termos

def dominio(equacao: str):
    y = 0.05
    arr = []
    for _ in range(20):
      arr.append(y)
      y += 1/20
    return arr

def somatorio(equacao: str, N: int | str, dominio: list):
    value = []
    match equacao:
        case 'dipolo':
            for x in dominio:
                eq = 0
                if N != 'original':
                    for n in range(N + 1):  # Número de vezes expandindo
                        u = Symbol('u')

                        f = u ** (n + 1)
                        g = f
                        eq += (diff(f, u) * (-1)**n) - diff(g, u)   # Expandindo
                        eq = eq.subs(u, x)
                else:
                    eq += ((1 + x)**(-2)) - ((1 - x)**(-2)) # Sem expandir
                value.append(eq)

        case 'quadrupolo':
            for x in dominio:
                eq = 0
                if N != 'original':
                    for n in range(N + 1):
                        u = Symbol('u')

                        f = u ** (n + 1)
                        g = f
                        eq += (diff(f, u) * ((-1) ** n) + diff(g, u))   # Expandindo
                        if n == 0:
                            eq += - (2 * diff(1 ** -2, u, n).subs(u, 0))
                        eq = eq.subs(u, x)
                else:
                    eq = ((1 - x)**(-2)) + ((1 + x)**(-2)) - (2 * (1**(-2)))    # Sem expandir
                value.append(eq)

        case _:
            raise Exception("Equação Inválida")
    return value


def pontos(equacao: str, data: bool):
    dicio = {
        "Px": [],
        "Py": {
            "5": [],
            "10": [],
            "30": [],
            "original": []
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

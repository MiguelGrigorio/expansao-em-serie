from sympy import Symbol, diff, exp, pretty_print, factorial
from math import pi


x = Symbol('x')
n = Symbol('n')
hx = x * exp(-2*x)
x0 = 0

dominio1 = []
dominio2 = []
d1 = 0
d2 = 0

for p in range(20):
    dominio1.append(d1)
    dominio2.append(d2)
    d1 += 2*pi/20
    d2 += 4/20
    d2 = round(d2, 2)

dominios = [dominio1, dominio1, dominio2]
with open('data.dat', 'w') as data:
    seq = 0
    for n in range(5):
        seq += ((-1)**n) * (x**((2 * n) + 1)) / (factorial((2 * n) + 1))
    for X in dominios[0]:
        data.write(f'{X}\t{seq.subs(x, X)}\n')

    data.write('\n')

    seq = 0
    for n in range(10):
        seq += ((-1)**n) * (x**((2 * n) + 1)) / (factorial((2 * n) + 1))
    for X in dominios[0]:
        data.write(f'{X}\t{seq.subs(x, X)}\n')

    data.write('\n')

    seq = 0
    for n in range(30):
        seq += ((-1)**n) * (x**((2 * n) + 1)) / (factorial((2 * n) + 1))
    for X in dominios[0]:
        data.write(f'{X}\t{seq.subs(x, X)}\n')

    data.write('\n\n')

    seq = 0
    for n in range(5):
        seq += ((-1)**n) * (x**(2*n)) / (factorial(2*n))
    for X in dominios[1]:
        data.write(f'{X}\t{seq.subs(x, X)}\n')

    data.write('\n')

    seq = 0
    for n in range(10):
        seq += ((-1)**n) * (x**(2*n)) / (factorial(2*n))
    for X in dominios[1]:
        data.write(f'{X}\t{seq.subs(x, X)}\n')

    data.write('\n')

    seq = 0
    for n in range(30):
        seq += ((-1)**n) * (x**(2*n)) / (factorial(2*n))
    for X in dominios[1]:
        data.write(f'{X}\t{seq.subs(x, X)}\n')

    data.write('\n\n')

    seq = 0
    for n in range(5):
        seq += ((diff(hx, x, n).subs(x, x0) * (x - x0)**n) / factorial(n))
    for X in dominios[2]:
        data.write(f'{X}\t{seq.subs(x, X)}\n')

    data.write('\n')

    seq = 0
    for n in range(10):
        seq +=((diff(hx, x, n).subs(x, x0) * (x - x0)**n) / factorial(n))
    for X in dominios[2]:
        data.write(f'{X}\t{seq.subs(x, X)}\n')

    data.write('\n')

    seq = 0
    for n in range(30):
        seq += ((diff(hx, x, n).subs(x, x0) * (x - x0)**n) / factorial(n))
    for X in dominios[2]:
        data.write(f'{X}\t{seq.subs(x, X)}\n')

    data.write('\n\n')
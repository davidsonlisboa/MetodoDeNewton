#Nome: Davidson Lisboa Della Piazza
#RA: 169786

import numpy as np
import sympy as sym
import math as math

x = sym.Symbol('x')

#definindo a funcao que sera estudada
def funcao(y):
    global x
    #funcao da questao A
    f = 1+(x**3)-(1/x)
    #funcao da questao B
    #f = (math.pi) - 1/x
    #funcao da questao c1
    #f = x**(1/3)
    #funcao da questao c2
    #f = (x**3) - 5*x
    #funcao da questao c3
    #f = (x**3) - (2*x) + 2
    return f.subs(x, y).evalf()

#metodo utilizado para derivar as funcoes
def dnf(f, chute):
    global x
    f = sym.diff(f)
    return f.subs(x, chute).evalf()


#Inicio do metodo de Newton
chute = 5
e = 1e-5
while (abs(funcao(chute))>e):
    chute = chute - funcao(chute)/dnf(funcao(x), chute)
    print(chute)

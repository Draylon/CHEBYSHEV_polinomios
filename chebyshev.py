

#   >>>>       https://github.com/Draylon/CHEBYSHEV_polinomios      <<<<<



import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
x= symbols('x')

def chebyshev_primeira_ordem(n):
    if n <= 0:
        return '1'
    if n == 1:
        return 'x'
    return '((2*x)*('+chebyshev_primeira_ordem(n-1)+')-('+chebyshev_primeira_ordem(n-2)+'))'

def chebyshev_segunda_ordem(n):
    if n == 0:
        return "1"
    if n == 1:
        return "2*x"
    return "2*x*("+chebyshev_segunda_ordem(n-1)+")-("+chebyshev_segunda_ordem(n-2)+")"


n = 6

#xv = np.linspace(-1,1,35) #lista de pontos de x
for i in range(0,n):
    
    y1s=chebyshev_primeira_ordem(i) #pegando a função de primeira ordem do chebyshev como string
    #y2s=chebyshev_segunda_ordem(i)  #esse aqui é o de segunda ordem
    #print(y1s)
    if(i % 2) != 0 and len(y1s) > 1:
        y1s = str(simplify(y1s))
        y1s = y1s[2:]
        y1s = simplify(y1s)
        print(simplify(f'{y1s}*{x}'))
        print( [simplify(f'{y1s}').coeff(x,ii-1) for ii in range(i,0,-1)] ) # aqui, pega a string, simplifica e lista os coeficientes
    else:
        y1s = simplify(str(y1s))
        print(y1s)
        print( [simplify(f'{y1s}').coeff(x,ii) for ii in range(i,0,-1)] ) # aqui, pega a string, simplifica e lista os coeficientes

    print()
    #print(y1s)
    #printar no console
    
    #essa parte desenha um gráfico
    '''
    y1v=[eval(y1s) for x in xv] # interpretando as funções, e gerando uma lista de pontos pra plotar
    plt.plot(xv, y1v, '-b') # joga os pontos da primeira ordem
plt.title('CHEBYSHEV')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.grid()
plt.show()

'''

# >.<'



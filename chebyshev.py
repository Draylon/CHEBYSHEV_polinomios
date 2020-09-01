
import math
import matplotlib.pyplot as plt
import numpy as np

def chev_cos(n,x):
    if chebyshev_primeira_ordem(n,math.cos(x)) == math.cos(n*x):
        return 1
    return 0

def chebyshev_primeira_ordem(n):
    if n == 0:
        return "1"
    if n == 1:
        return "x"
    return "2*x*("+chebyshev_primeira_ordem(n-1)+")-("+chebyshev_primeira_ordem(n-2)+")"

def chebyshev_segunda_ordem(n):
    if n == 0:
        return "1"
    if n == 1:
        return "2*x"
    return "2*x*("+chebyshev_segunda_ordem(n-1)+")-("+chebyshev_segunda_ordem(n-2)+")"

xv = np.linspace(-1,1,30)
for i in range(5):
    y1s=chebyshev_primeira_ordem(i)
    y2s=chebyshev_segunda_ordem(i)
    print(y2s)
    y1v=[eval(y1s) for x in xv]
    y2v=[eval(y2s) for x in xv]
    #plt.plot(xv, y1v, '-b')
    plt.plot(xv, y2v, '-r')
plt.title('Stonks')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.grid()
plt.show()
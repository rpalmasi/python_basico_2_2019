# crear un código que calcule las soluciones de la equación cuadrática
# ax2 + bx + c = 0

import math

a = float(input('Favor ingresar a'))
b = float(input('Favor ingresar b'))
c = float(input('Favor ingresar c'))

discriminante= b**2-4*a*c
print('discriminante',discriminante)

if discriminante <0:
    raiz = math.sqrt(-discriminante) * complex(0,1)
else:
    raiz = math.sqrt(discriminante)

#raiz = math.sqrt(discriminante)

x1= (-b + raiz)/(2*a)
x2= (-b - raiz)/(2*a)
print(x1,x2)



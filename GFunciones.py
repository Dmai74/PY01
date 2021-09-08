# -----------------------------------
# importamos librerías con funciones predefinidas
# ----------------------------------

import datetime 
import math
import matplotlib.pyplot as plt
import numpy as np


def MiFuncion (X):  
    Resultado = math.sin(X)
    return Resultado
    
# ----------------------------
# NUESTRO PROGRAMA
# ----------------------------
print ('Hi, Seba!')
print ('================')

# armamos los arreglos de los ejes cartesianos X e Y

print ('Ingrese el rango valores de X')
n = int(input('Desde: '))
m = int(input('Hasta: '))
print ('Rango: ', m-n)

x = np.zeros(m-n+1)
y = np.zeros(m-n+1)

c= float (n)

for i in range (m-n+1):
      x.itemset(i,c)
      y.itemset(i,MiFuncion(c))
      c=c+1 
      print (i, ' x [',i,'] = ', x[i], ' y [',i,'] = ', y[i])

print (x)
print (y)

plt.plot(y)
plt.show()


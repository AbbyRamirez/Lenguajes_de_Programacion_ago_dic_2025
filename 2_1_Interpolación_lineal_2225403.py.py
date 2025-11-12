import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x = sp.Symbol("x") #hacer x el simbolo
i = 0
equis = []#listas para graficar
ye = []
error = 10
a = float(input("Escribe el valor x1: "))#puntos a interpolar
b = float(input("Escribe el valor y1: "))
c = float(input("Escribe el valor x2: "))
d = float(input("Escribe el valor y2: "))
# Ecuación de interpolación lineal
Ec = b + ((d-c)/(b-a))*(x-a)
EXP = sp.sympify(Ec)
entreab = float(input("valor a interpolar: "))
Fab = float(EXP.subs(x, entreab))#sustituir x en el valor a interpolar
print(Fab,Ec)
# Llenar listas equis y ye para graficar 
for i in np.linspace(min(a, c) - 1, max(a, c) + 1, 50):
    equis.append(i)
    ye.append(float(EXP.subs(x, i)))
#Gráfica
plt.figure(figsize=(7, 5))
plt.plot(equis, ye, label="Interpolación lineal", color='blue')
plt.scatter([a, c], [b, d], color='red', label='Puntos dados')
plt.scatter(entreab, Fab, color='green', marker='o', label=f'Punto interpolado ({entreab}, {Fab:.2f})')
plt.title("Método de Interpolación Lineal")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

print("Programa terminado")







import numpy as np
import matplotlib.pyplot as plt

# Pedir los puntos
a = float(input("Escribe el valor x1: "))
b = float(input("Escribe el valor y1: "))
c = float(input("Escribe el valor x2: "))
d = float(input("Escribe el valor y2: "))
e = float(input("Escribe el valor x3: "))
f = float(input("Escribe el valor y3: "))
# Matriz de coeficientes
Matiz = np.array([
    [a**2, a, 1],
    [c**2, c, 1],
    [e**2, e, 1]
])
matizind = np.array([b, d, f])#matriz de las ordenadas
resp = np.linalg.solve(Matiz, matizind) #Resolver la matriz para encontrar los coeficientes
print(resp)
A, B, C = resp
x_vals = np.linspace(min(a, c, e) - 2, max(a, c, e) + 2, 200)#tabular para graficar
y_vals = A * x_vals**2 + B * x_vals + C #construir la ecuación
# Graficar
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='Parábola ajustada', color='blue')
plt.scatter([a, c, e], [b, d, f], color='red', label='Puntos dados', zorder=5)
plt.title('Parábola que pasa por tres puntos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
print("\nPrograma terminado :D")

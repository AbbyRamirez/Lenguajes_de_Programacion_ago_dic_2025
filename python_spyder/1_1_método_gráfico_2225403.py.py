import numpy as np
import matplotlib.pyplot as plt
x = [] #listas para las coordenadas a graficar
y = []
while True: #Ciclo para conseguir datos 
    # Pedir coordenadas
    xi = float(input("Diga su coordenada x: "))
    yi = float(input("Diga su coordenada y: "))

    x.append(xi)
    y.append(yi)

    # Condición de salida
    fin = input("Presione 1 para terminar, o cualquier otra tecla para continuar: ")
    if fin == "1":
        break
# Graficar los puntos dados
plt.scatter(x, y, color='red', label='Datos experimentales')
# Ajuste polinómico (grado 2 o 3)
grado = 2
coef = np.polyfit(x, y, grado)
p = np.poly1d(coef)
# Generar valores para la curva ajustada
x_line = np.linspace(min(x), max(x), 200)
y_line = p(x_line)
# Mostrar la curva
plt.plot(x_line, y_line, color='blue', label=f'Ajuste polinómico de grado {grado}')
plt.title('Método gráfico de aproximación polinómica')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar la ecuación encontrada
print("\nEcuación aproximada del polinomio:")
print(p)

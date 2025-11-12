import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def newton_poly(x_vals, y_vals): #función para las divisiones
   
    n = len(x_vals)
    x = sp.Symbol('x')
    # Matriz de diferencias divididas
    dd = np.zeros((n, n))
    dd[:, 0] = y_vals

    for j in range(1, n):
        for i in range(n - j):
            dd[i][j] = (dd[i + 1][j - 1] - dd[i][j - 1]) / (x_vals[i + j] - x_vals[i])

    # Construcción del polinomio
    P = dd[0][0]
    term = 1
    for j in range(1, n):
        term *= (x - x_vals[j - 1])
        P += dd[0][j] * term

    return sp.simplify(P)

if __name__ == "__main__":
    n = int(input("Ingrese el número de puntos: "))

    x_data = []#listas para la sumatoria de los valores
    y_data = []

    print("\nIngrese las coordenadas (x, y):")
    for i in range(n):
        x_i = float(input(f"  x[{i}]: "))
        y_i = float(input(f"  y[{i}]: "))
        x_data.append(x_i)#listas para los puntos
        y_data.append(y_i)

    # Calcular el polinomio de Newton
    P_sym = newton_poly(x_data, y_data)
    print("\nPolinomio:")
    print(P_sym)

    print("\nPolinomio expandido:")# imprimir el polinomio
    print(sp.expand(P_sym))

    # desimbolizar la expr
    P_func = sp.lambdify(sp.Symbol('x'), P_sym, modules=['numpy'])

    # Valores para graficar
    x_plot = np.linspace(min(x_data) - 1, max(x_data) + 1, 400)
    y_plot = P_func(x_plot)

    # Gráfica 
    plt.figure(figsize=(8, 5))
    plt.plot(x_plot, y_plot, label='Polinomio de Newton', color='blue')
    plt.scatter(x_data, y_data, color='red', zorder=5, label='Puntos dados')
    plt.title('Interpolación de Newton')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.legend()
    plt.grid(True)

    # Mostrar la ecuación en la gráfica
    plt.text(min(x_data), max(y_data), f"P(x) = {sp.N(P_sym, 3)}", fontsize=10, color='black')

    plt.show()




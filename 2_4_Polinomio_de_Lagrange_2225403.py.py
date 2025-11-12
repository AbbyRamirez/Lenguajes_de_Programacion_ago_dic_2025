import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def lagrange_poly(x_vals, y_vals):
    """Función para las sumatorias y productorias"""
    x = sp.Symbol('x')
    n = len(x_vals)
    P = 0
    for i in range(n):
        Li = 1
        for j in range(n):
            if j != i:
                Li *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        P += y_vals[i] * Li
    return sp.simplify(P)

if __name__ == "__main__":
    print("Polinomio de Interpolación de Lagrange")
    n = int(input("Ingrese el número de puntos: "))

    x_data = []#listas para la productorioa
    y_data = []

    print("\nIngrese las coordenadas (x, y):")
    for i in range(n):
        x_i = float(input(f"  x[{i}]: "))
        y_i = float(input(f"  y[{i}]: "))
        x_data.append(x_i)
        y_data.append(y_i)

    # Construir polinomio
    P_sym = lagrange_poly(x_data, y_data)
    print("\nPolinomio de Lagrange:")
    print(P_sym)

    print("\nPolinomio expandido:")
    print(sp.expand(P_sym))

    # Convertir a función numérica
    P_func = sp.lambdify(sp.Symbol('x'), P_sym, modules=['numpy'])

    # Crear valores para graficar
    x_plot = np.linspace(min(x_data) - 1, max(x_data) + 1, 400)
    y_plot = P_func(x_plot)

    # Gráfica 
    plt.figure(figsize=(8, 5))
    plt.plot(x_plot, y_plot, label='Polinomio de Lagrange', color='blue')
    plt.scatter(x_data, y_data, color='red', zorder=5, label='Puntos dados')
    plt.title('Interpolación de Lagrange')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.legend()
    plt.grid(True)

    # Mostrar la ecuación en la gráfica (abreviada)
    eq_text = sp.pretty(sp.expand(P_sym))
    plt.text(min(x_data), max(y_data), f"P(x) = {sp.simplify(P_sym)}", fontsize=10, color='black')

    plt.show()






import numpy as np
import pandas as pd#para tablas chidas
import matplotlib.pyplot as plt

def regresion_cuadratica(x_vals, y_vals):
    """
    Hace el trabajo de hacer las sumatorias y los sistemas de ecuaciones
    """
    n = len(x_vals)
    x = np.array(x_vals, dtype=float)
    y = np.array(y_vals, dtype=float)

    # Cálculos intermedios
    x2 = x ** 2
    x3 = x ** 3
    x4 = x ** 4
    xy = x * y
    x2y = x2 * y

    # Sumatorias necesarias
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x2)
    sum_x3 = np.sum(x3)
    sum_x4 = np.sum(x4)
    sum_xy = np.sum(xy)
    sum_x2y = np.sum(x2y)

    # Sistema de ecuaciones normal:
    
    A = np.array([
        [n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ])
    B = np.array([sum_y, sum_xy, sum_x2y])

    # Resolver el sistema
    a, b, c = np.linalg.solve(A, B)

    # Crear tabla con pandas
    tabla = pd.DataFrame({
        'x': x,
        'y': y,
        'x²': x2,
        'x³': x3,
        'x⁴': x4,
        'xy': xy,
        'x²y': x2y
    })

    # Fila de sumatorias
    sum_row = pd.DataFrame({
        'x': [sum_x],
        'y': [sum_y],
        'x²': [sum_x2],
        'x³': [sum_x3],
        'x⁴': [sum_x4],
        'xy': [sum_xy],
        'x²y': [sum_x2y]
    }, index=['Σ'])

    tabla = pd.concat([tabla, sum_row])

    # Mostrar tabla y resultados
    print("\n=== TABLA DE CÁLCULOS DE REGRESIÓN CUADRÁTICA ===\n")
    print(tabla)

    print("\n--- SUMATORIAS ---")
    print(f"Σx   = {sum_x:.4f}")
    print(f"Σy   = {sum_y:.4f}")
    print(f"Σx²  = {sum_x2:.4f}")
    print(f"Σx³  = {sum_x3:.4f}")
    print(f"Σx⁴  = {sum_x4:.4f}")
    print(f"Σxy  = {sum_xy:.4f}")
    print(f"Σx²y = {sum_x2y:.4f}")

    print("\n--- COEFICIENTES DEL MODELO ---")
    print(f"a = {a:.6f}")
    print(f"b = {b:.6f}")
    print(f"c = {c:.6f}")
    print(f"Modelo ajustado: y = {a:.4f} + {b:.4f}x + {c:.4f}x²")

    # Calcular el coeficiente de determinación R²
    y_pred = a + b * x + c * x2
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    print(f"Coeficiente de determinación (R²) = {r2:.4f}")

    # --- Gráfica ---
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='red', label='Datos experimentales')

    x_plot = np.linspace(min(x), max(x), 200)
    y_plot = a + b * x_plot + c * x_plot**2
    plt.plot(x_plot, y_plot, color='blue', label=f'y = {a:.2f} + {b:.2f}x + {c:.2f}x²')

    plt.title('Regresión Cuadrática por Mínimos Cuadrados')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Mostrar la ecuación en la gráfica
    plt.text(min(x), max(y), f"y = {a:.2f} + {b:.2f}x + {c:.2f}x²\nR² = {r2:.4f}",
             fontsize=10, color='black', bbox=dict(facecolor='white', alpha=0.7))
    plt.show()


if __name__ == "__main__":
    print("=== REGRESIÓN CUADRÁTICA POR MÍNIMOS CUADRADOS ===")
    n = int(input("Ingrese el número de puntos: "))

    x_data = []
    y_data = []

    print("\nIngrese las coordenadas (x, y):")
    for i in range(n):
        x_i = float(input(f"  x[{i+1}]: "))
        y_i = float(input(f"  y[{i+1}]: "))
        x_data.append(x_i)
        y_data.append(y_i)

    regresion_cuadratica(x_data, y_data)



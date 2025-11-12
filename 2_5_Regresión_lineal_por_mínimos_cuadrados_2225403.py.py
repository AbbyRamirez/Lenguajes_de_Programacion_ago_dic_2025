import numpy as np
import pandas as pd #para hacer la tabla (no pude con numpy :c)
import matplotlib.pyplot as plt

def minimos_cuadrados_lineal(x_vals, y_vals):
    """
    Función para las sumatorias y la tabla de ellas
    """
    n = len(x_vals)
    x = np.array(x_vals, dtype=float)
    y = np.array(y_vals, dtype=float)

    # Cálculos intermedios
    x2 = x ** 2
    xy = x * y

    # Sumatorias
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x2)
    sum_xy = np.sum(xy)

    # Cálculo de coeficientes
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a = (sum_y - b * sum_x) / n

    # Crear tabla de datos
    tabla = pd.DataFrame({
        'x': x,
        'y': y,
        'x²': x2,
        'xy': xy
    })

    # Agregar fila de sumatorias
    sum_row = pd.DataFrame({
        'x': [sum_x],
        'y': [sum_y],
        'x²': [sum_x2],
        'xy': [sum_xy]
    }, index=['Σ'])

    tabla = pd.concat([tabla, sum_row])# tabla chida

    print("\n=== TABLA DE CÁLCULOS DE MÍNIMOS CUADRADOS ===\n")
    print(tabla)

    print("\n--- SUMATORIAS ---")
    print(f"Σx  = {sum_x:.4f}")
    print(f"Σy  = {sum_y:.4f}")
    print(f"Σx² = {sum_x2:.4f}")
    print(f"Σxy = {sum_xy:.4f}")

    print("\n--- COEFICIENTES DEL MODELO ---")
    print(f"a (intercepto) = {a:.4f}")
    print(f"b (pendiente)  = {b:.4f}")
    print(f"Modelo ajustado: y = {a:.4f} + {b:.4f}x")

    # Calcular coeficiente
    y_pred = a + b * x
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    print(f"Coeficiente de determinación (R²) = {r2:.4f}")

    # Gráfiquilla
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='red', label='Datos experimentales')
    plt.plot(x, y_pred, color='blue', label=f'y = {a:.2f} + {b:.2f}x')
    plt.title('Ajuste Lineal por Mínimos Cuadrados')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Mostrar ecuación en la gráfica
    plt.text(min(x), max(y), f"y = {a:.2f} + {b:.2f}x\nR² = {r2:.4f}",
             fontsize=10, color='black', bbox=dict(facecolor='white', alpha=0.6))
    plt.show()


if __name__ == "__main__":
    print("AJUSTE LINEAL POR MÍNIMOS CUADRADOS ")
    n = int(input("Ingrese el número de puntos: "))

    x_data = []
    y_data = []

    print("\nIngrese las coordenadas (x, y):")
    for i in range(n):
        x_i = float(input(f"  x[{i+1}]: "))
        y_i = float(input(f"  y[{i+1}]: "))
        x_data.append(x_i)
        y_data.append(y_i)

    minimos_cuadrados_lineal(x_data, y_data)



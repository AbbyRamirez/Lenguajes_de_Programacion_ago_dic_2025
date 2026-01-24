#1
import numpy as np
import matplotlib.pyplot as plt
#2
m = int(input("¿Cuántos puntos tienes? "))
x = np.zeros(m)
y = np.zeros(m)
for i in range(m):
    x[i] = float(input(f"x[{i+1}]: "))
    y[i] = float(input(f"y[{i}]: "))
#3
x2 = x * x
xy = x * y
m = len(x)
Sx  = np.sum(x)
Sy  = np.sum(y)
Sxx = np.sum(x * x)
Sxy = np.sum(x * y)
denom = m * Sxx - Sx**2
a = (m * Sxy - Sx * Sy) / denom
b = (Sy - a * Sx) / m
#4
print("\nTabla de valores y sumatorias:")
print(f"{"i":>4} | {"x":>8} | {"y":>8} | {"x²":>8} | {"xy":>8}")
for i in range(m):
    print(f"{i+1:>4} | {x[i]:>8.2f} | {y[i]:>8.2f} | {x2[i]:>8.2f} | {xy[i]:>8.2f}")
print(f"suma | {Sx:>8.2f} | {Sy:>8.2f} | {Sxx:>8.2f} | {Sxy:>8.2f}")
#5
print("\nResultados:")
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print("\nEcuación ajustada:")
print(f"y = {a:.4f} x + {b:.4f}")
#6
x_plot = np.linspace(min(x) - 1, max(x) + 1, 150)
y_plot = a * x_plot + b
#7
plt.axhline(0, color="gray", linestyle="--", label="Ejes coordenados")
plt.axvline(0, color="gray", linestyle="--")
plt.scatter(x, y, color="goldenrod", label="Datos", zorder=5)
plt.plot(x_plot, y_plot, color="orchid", linewidth=2, label=f"Ajuste: y = {a:.4f} x + {b:.4f}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regresión lineal por mínimos cuadrados")
plt.grid(True, linestyle="--")
plt.legend()
plt.show()


import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
error=10
x = sp.Symbol("x") #hacer simboo a la x
i = 0
Xi=[]
Funcion = input("Escriba en lenguaje python la función a aproximar: ")
F = sp.sympify(Funcion)#simbolizar expr
a = float(input("Escribe el valor inicial para aproximar la raíz: "))
f = sp.diff(F,x)#derivar a la expr
Fequis = sp.lambdify(x, F, 'numpy')#desimbolizar a las expr
fequis = sp.lambdify(x, f, 'numpy')

while error > 0.01 and i < 5:
    
    Fa = F.subs(x, a)#evaluar en a
    fa = f.subs(x, a)#evaluar en b
    
    b = a - ((Fa*fa)/((fa**2)-(Fa*fa)))#método modificado
    Xi.append(a)#agregar los resultados
    error = abs((b - a)/b) * 100#calcular el error
    a = b  
    
    # Rango para graficar
    x_vals = np.linspace(float(min(Xi)) - 1, float(max(Xi)) + 1, 20)
    y_vals = Fequis(x_vals)
    y_der = fequis(x_vals)
    
    # Graficar función y derivada
    plt.figure(figsize=(10,6))
    plt.plot(x_vals, y_vals, label='f(x)', color='purple')
    plt.plot(x_vals, y_der, label="f'(x)", color='magenta', linestyle='--')
    
    # Graficar puntos iterados
    for xi in Xi:
        plt.plot(xi, Fequis(xi), 'ro')
    plt.plot(Xi[-1], Fequis(Xi[-1]), 'mo', label='Xn-1')
    
    # Graficar recta tangente en el último punto
    x0 = Xi[-1]
    y0 = Fequis(x0)
    m = fequis(x0)
    tangente = m * (x_vals - x0) + y0
    plt.plot(x_vals, tangente, label=f'Tangente en x={x0:.4f}', color='cyan')
    
    # Ajustes finales
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.title(f'Newton-Raphson Modificado: Iteración {i+1}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    i += 1

print("programa terminado")



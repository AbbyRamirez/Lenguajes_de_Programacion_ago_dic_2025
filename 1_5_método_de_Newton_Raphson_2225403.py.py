import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
error=10
x = sp.Symbol("x")#hacer x un simbolo
i = 0 #control para el ciclo
Xi=[] #Lista de aproximaciones
Funcion = input("Escriba en lenguaje python la función a aproximar: ")
F = sp.sympify(Funcion) #hacer la expresión un símbolo
a = float(input("Escribe el valor inicial para aproximar la raíz: "))
f = sp.diff(F,x) #derivar con respecto a x la expresión
Fequis = sp.lambdify(x, F, 'numpy') #desimbolizar la expresión
fequis = sp.lambdify(x, f, 'numpy')#desimbolizar su derivada

while error > 0.1 and i < 5: #ciclo para las iteraciones
    
    Fa = F.subs(x, a) #sustituir el valor en la función y su derivada
    fa = f.subs(x, a)
    
    b = a - (Fa / fa) #Método newton raphson
    Xi.append(a) #añadir resultado a la lista
    error = abs((b - a)/b) * 100 # calcular error
    a = b  # iterar el proceso
    
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
    
    # Graficar recta tangente 
    x0 = Xi[-1]
    y0 = Fequis(x0)
    m = fequis(x0)
    tangente = m * (x_vals - x0) + y0
    plt.plot(x_vals, tangente, label=f'Tangente en x={x0:.4f}', color='cyan')
    
    # Configuación de la gráfica
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.title(f'Newton-Raphson: Iteración {i+1}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    i += 1 #control del ciclo

print("programa terminado :D")
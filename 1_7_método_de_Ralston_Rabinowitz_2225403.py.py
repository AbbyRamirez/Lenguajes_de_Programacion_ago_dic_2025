import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
error=10
x = sp.Symbol("x") #hacer x un simbolo
i = 0
Xi=[]
Funcion = input("Escriba en lenguaje python la función a aproximar: ")
F = sp.sympify(Funcion) # hacer la expr un símbolo
a = float(input("Escribe el valor inicial para aproximar la raíz: "))
m = float(input("Escribe el valor de la multiplicidad: "))
f = sp.diff(F,x)# derivar la expr
Fequis = sp.lambdify(x, F, 'numpy')#hacer la expr y su derivada no simbolos
fequis = sp.lambdify(x, f, 'numpy')

while error > 0.1 and i < 5: # si las condiciones se cumplen el ciclo sigue
    
    Fa = F.subs(x, a) #sustituir las expr en a y b
    fa = f.subs(x, a)
    
    b = a - ((m*(Fa*fa)/((fa**2)-(Fa*fa)))) #método ralston rabinowitz
    Xi.append(a)
    error = abs((b - a)/b) * 100 #calcular error
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



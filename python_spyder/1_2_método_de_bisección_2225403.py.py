import sympy as sp #librerias importadas para el programa
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol("x") #Hacemos a la literal x un símbolo 

i = 0 #determinamos un control de iteraciones para mejores valores
equis = [] #lista de los valores de x
ye = [] #lista de los valores de y
error = 10 #porcentaje de error
Expresion = input("Escriba en lenguaje python la función a aproximar: ") 
EXP = sp.sympify(Expresion) #hacemos la expresión un símbolo
a = float(input("Escribe el valor inicial para aproximar la raíz (a): "))
b = float(input("Escribe el valor inicial para aproximar la raíz (b): "))

g_func = sp.lambdify(x, EXP, modules=['numpy']) #desimbolizamos a la expresión para graficarla

while error > 0.1 and i < 5: #mientras la tolerancia sea mayor y las iteraciones menor que 5 correrá el programa
    # Evaluar función
    FA = float(EXP.subs(x, a))
    FB = float(EXP.subs(x, b))

    # Método de la bisección
    c = 0.5*(a+b)
    FC = float(EXP.subs(x, c))
    error = abs(c - a)

    print(f"Iteración {i}: a={a:.5f}, b={b:.5f}, c={c:.5f}, f(c)={FC:.5f}")# Las 5 aproximaciones

    fig, ax = plt.subplots(figsize=(8, 6)) #Configuración y propiedades de la gráfica
    X = np.linspace(a - 2, b + 2, 400)
    Y = g_func(X)

    # Gráfica de F(x)
    ax.plot(X, Y, 'b', label=f'f(x) = {Expresion}', linewidth=2)
    ax.axhline(0, color='black', linewidth=1)

    # Gráfica de los puntos y las rectas
    ax.plot(a, FA, 'ro', markersize=8, label='Punto a')
    ax.plot(b, FB, 'go', markersize=8, label='Punto b')
    ax.plot(c, FC, 'mo', markersize=8, label='Punto c (nuevo)')

    # Etiqueta de los puntos
    ax.text(a, FA, f"  a={a:.3f}", color='red', fontsize=9, ha='left', va='bottom')
    ax.text(b, FB, f"  b={b:.3f}", color='green', fontsize=9, ha='left', va='bottom')
    ax.text(c, FC, f"  c={c:.3f}", color='magenta', fontsize=9, ha='left', va='bottom')

    # Propiedades y características de las gráficas
    ax.set_title(f"Iteración {i}", fontsize=14, fontweight='bold')
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend(loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.6)

    # Mostrar figura 
    plt.show(block=False)

    #Actualización de intervalos 
    if FA * FC < 0:
        b = c
    else:
        a = c

    i += 1 # control del ciclo

print("Programa terminado")




import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


x = sp.Symbol("x")# hacer simbolo a x

i = 0
equis = []
ye = []
error = 10
Expresion = input("Escriba en lenguaje python la función a aproximar: ")
EXP = sp.sympify(Expresion)# hacer la expresión un símbolo
a = float(input("Escribe el valor inicial para aproximar la raíz (a): "))
b = float(input("Escribe el valor inicial para aproximar la raíz (b): "))

g_func = sp.lambdify(x, EXP, modules=['numpy'])


while error > 0.01 and i < 5: # si las condiciones complen el bucle sigue
    # Evaluar función
    FA = float(EXP.subs(x, a))
    FB = float(EXP.subs(x, b))
    
    # Método de la secante
    c = a - ((a-b)*FA)/(FA-FB)
    FC = float(EXP.subs(x, c))
    error = abs((c - a)/c)

    print(f"Iteración {i}: a={a:.5f}, b={b:.5f}, c={c:.5f}, f(c)={FC:.5f}")

    # --- Crear nueva figura por iteración ---
    fig, ax = plt.subplots(figsize=(8, 6))
    X = np.linspace(a - 2, b + 2, 400)
    Y = g_func(X)

    # Función
    ax.plot(X, Y, 'b', label=f'f(x) = {Expresion}', linewidth=2)
    ax.axhline(0, color='black', linewidth=1)

    # Puntos y secante
    ax.plot([a, b], [FA, FB], 'k--', label='Línea secante', linewidth=1)
    ax.plot(a, FA, 'ro', markersize=8, label='Punto a')
    ax.plot(b, FB, 'go', markersize=8, label='Punto b')
    ax.plot(c, FC, 'mo', markersize=8, label='Punto c (nuevo)')

    # Etiquetas de puntos
    ax.text(a, FA, f"  a={a:.3f}", color='red', fontsize=9, ha='left', va='bottom')
    ax.text(b, FB, f"  b={b:.3f}", color='green', fontsize=9, ha='left', va='bottom')
    ax.text(c, FC, f"  c={c:.3f}", color='magenta', fontsize=9, ha='left', va='bottom')

    # configuración
    ax.set_title(f"Iteración {i}", fontsize=14, fontweight='bold')
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend(loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.6)

    plt.show(block=False)

    #  Actualización de intervalos
    if FA * FC < 0:
        b = c
    else:
        a = c

    i += 1

print("Programa terminado")


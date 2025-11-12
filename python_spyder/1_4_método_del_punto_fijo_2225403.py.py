import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Variable simbólica
x = sp.Symbol("x")

# Inicialización
i = 0
equis = [] #lista de las x
ye = [] #lista de las y
error = 10

Expresion = input("Escriba en lenguaje python la función a aproximar ya despejada: ")
EXP = sp.sympify(Expresion) # hacer la expresión un símbolo
a = float(input("Escribe el valor inicial para aproximar la raíz: "))

g_func = sp.lambdify(x, EXP, modules=['numpy']) # desimbolizar la expresión

while error > 0.001 and i < 5: #si las condiciones se cumplen el ciclo continua
    b = EXP.subs(x, a) #evalua gx         
    error = abs(b - a)  #calcula el error
    print(i, a, b)

    equis.append(float(b)) #guardan las coordenadas para graficar
    ye.append(float(b))          

    a = b
    
    xg = np.linspace(min(equis)-1, max(equis)+1, 200)#limites de la gráfica
    yg = g_func(xg)

    plt.figure(figsize=(7,6)) #configuración de la gráfica
    plt.plot(xg, yg, label='g(x)', color='blue')
    plt.plot(xg, xg, label='y = x', color='red', linestyle='--')

    # Dibujar puntos de iteración
    plt.scatter(equis, ye, color='green', zorder=5, label='Iteraciones')

    # Dibujar líneas de conexión (cobweb plot)
    for n in range(len(equis)-1):
        plt.plot([equis[n], equis[n]], [equis[n], ye[n]], 'k--', alpha=0.5)
        plt.plot([equis[n], equis[n+1]], [ye[n], ye[n]], 'k--', alpha=0.5)

    plt.title('Método del Punto Fijo')
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    i += 1
print("progama terminado")   

import random

print("RANDOM FOREST PARA UNA CLASIFICACIÓN")

# 1. Ingresar datos
n = int(input("¿Cuántos datos tienes? "))

x = []
y = []

for i in range(n):
    xi = float(input(f"Ingrese el valor de x{i+1}: "))
    yi = int(input(f"Ingrese la clase (0 o 1) para x{i+1}: "))
    x.append(xi)
    y.append(yi)

# 2. Función para crear un árbol de decisión simple
def arbol_decision(x, y):
    umbral = random.choice(x)
    izquierda = [] 
    derecha = []

    for i in range(len(x)):
        if x[i] <= umbral:
            izquierda.append(y[i])
        else:
            derecha.append(y[i])
    # En este paso, el árbol "aprende" qué clase es más común en cada lado.
    if izquierda:
        clase_izq = max(set(izquierda), key=izquierda.count)
    else:
        clase_izq = 0
    if derecha:
        clase_der = max(set(derecha), key=derecha.count)
    else:
        clase_der = 1
    return umbral, clase_izq, clase_der

# 3. Crear varios árboles (el bosque)
def crear_bosque(x, y, num_arboles=7):
    bosque = []
    for _ in range(num_arboles):
        indices = []
        for j in range(len(x)):
            indice_aleatorio = random.randint(0, len(x) - 1)
            indices.append(indice_aleatorio)
        x_muestra = []
        y_muestra = []
        for i in indices:
            x_muestra.append(x[i])
            y_muestra.append(y[i])
        arbol = arbol_decision(x_muestra, y_muestra)
        bosque.append(arbol)
    return bosque
# 4. Hacer una predicción y mostrar los votos
def predecir(bosque, x_nuevo):
    votos = []
    print("\n Votaciones de los árboles ")
    i = 1
    for elemento in bosque:
        umbral = elemento[0]
        clase_izq = elemento[1]
        clase_der = elemento[2]
        
        if x_nuevo <= umbral:
            voto = clase_izq
        else:
            voto = clase_der
        print(f"Árbol {i}: umbral={umbral:.2f}, "
              f"izq={clase_izq}, der={clase_der}; vota: {voto}")
        votos.append(voto)
        i += 1
        if x_nuevo <= umbral:
            voto = clase_izq
        else:
            voto = clase_der
        votos.append(voto)
    prediccion = max(set(votos), key=votos.count)
    return prediccion

# 5. Crear el bosque y hacer la predicción
bosque = crear_bosque(x, y, num_arboles=7)

x_nuevo = float(input("\nIngrese el valor de x para clasificar: "))
prediccion = predecir(bosque, x_nuevo)

print(f"\nPredicción final para x = {x_nuevo}: Clase ≈ {prediccion}")

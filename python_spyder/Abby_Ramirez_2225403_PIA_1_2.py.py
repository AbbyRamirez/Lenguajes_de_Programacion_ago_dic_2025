import random #Librería para dar cartas y para el mal jugador

def valor_carta(carta):
    """Función para darles valores a las cartas que tienen letras""" 
    if carta in ['J', 'Q', 'K']:
        return 10
    elif carta == 'A':
        return 11  
    else:
        return int(carta)

def ajustar_ases(mano):
    """Convierte Ases de 11 a 1 si el total supera 21."""
    total = sum(valor_carta(c) for c in mano)
    ases = mano.count('A')
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

def penalizacion_especial(mano):
    """Aplica penalizaciones por As, Rey o Joker."""
    penalizacion = 0
    for c in mano:
        if c == 'A':
            penalizacion -= 10 #pierdes 10 pts
        elif c == 'K':
            penalizacion -= 7 #pierdes 7 pts
        elif c == 'J':
            penalizacion -= 5 #pierdes 5 pts
    return penalizacion

def repartir_carta():
    """Función que reparte las cartas, es decir el repartidor"""
    cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] #mazo de cartas
    return random.choice(cartas) #da cartas al azar a los 3 jugadores

def mostrar_mano(nombre, mano):
    """Muestra las cartas y los puntos de un ugador."""
    total = ajustar_ases(mano) #lista de puntos
    penal = penalizacion_especial(mano) #lista de puntos perdidos
    total_final = total + penal #puntos finales
    print(f"{nombre}: {', '.join(mano)} (Total: {total}) | Penalización: {penal} | Puntaje final: {total_final}")

def juego_21_tres_jugadores(): # Función para el titulo del programa
    print("Pierde de a  21 (3 JUGADORES, CON PENALIZACIONES) ")
    print(" Regla: A = -10 pts | K = -7 pt | J = -5 pt\n")

    # Inicializar manos de los 3 jugadores
    usuario = [repartir_carta(), repartir_carta()]
    bot_inteligente = [repartir_carta(), repartir_carta()]
    bot_aleatorio = [repartir_carta(), repartir_carta()]

    # Mostrar manos previas
    print(" Tus cartas:")
    mostrar_mano("Usuario", usuario)
    print("\nJugador 2 (inteligente):")
    mostrar_mano("Jugador 2", bot_inteligente)
    print("\nJugador 3 (aleatorio):")
    mostrar_mano("Jugador 3", bot_aleatorio)

    #Turno de jugar para el usuario
    while True:
        total_u = ajustar_ases(usuario)
        if total_u >= 21: #si llegas a más de 21 el juego se termina
            break
        accion = input("\n¿Quieres otra carta? (s/n): ").lower() #te pregunta por otra carta
        if accion == 's':
            usuario.append(repartir_carta())# si le dices s, te da otra carta
            mostrar_mano("Usuario", usuario) # de lo contario acaba el juego
        else:
            break

    # --- Turno del jugador 2 (consciente) ---
    while ajustar_ases(bot_inteligente) < 19:
        bot_inteligente.append(repartir_carta())

    # --- Turno del jugador 3 (aleatorio) ---
    while random.choice([True, False]) and ajustar_ases(bot_aleatorio) < 21:
        bot_aleatorio.append(repartir_carta())

    # Mostrar resultados
    print("\n RESULTADOS FINALES ")
    mostrar_mano("Usuario", usuario)
    mostrar_mano("Jugador 2 (inteligente)", bot_inteligente)
    mostrar_mano("Jugador 3 (aleatorio)", bot_aleatorio)

    #Calcular puntajes con pérdidas
    jugadores = {
        "Usuario": ajustar_ases(usuario) + penalizacion_especial(usuario),
        "Jugador 2 (inteligente)": ajustar_ases(bot_inteligente) + penalizacion_especial(bot_inteligente),
        "Jugador 3 (aleatorio)": ajustar_ases(bot_aleatorio) + penalizacion_especial(bot_aleatorio)
    }

    # Filtrar jugadores que no se pasaron
    jugadores_validos = {k: v for k, v in jugadores.items() if v <= 21}

    if not jugadores_validos:
        print("\n Todos se pasaron de 21. ¡Nadie gana!") #cuando nadie gana 
        return

    max_puntaje = max(jugadores_validos.values())
    ganadores = [k for k, v in jugadores_validos.items() if v == max_puntaje]

    print("\n GANADOR(ES):", ", ".join(ganadores)) #lista de ganadores y el podio
    print(f"Puntaje: {max_puntaje}")

if __name__ == "__main__":
    juego_21_tres_jugadores()



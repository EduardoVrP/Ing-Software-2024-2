def pedir_numero():
    entrada = -1
    while entrada == -1:
        try:
            entrada = int(input())
        except(ValueError):
            print("Lo ingresado no es un numero entero, ingresa el numero nuevamente.\n")
            entrada = -1
    
    return entrada

def pedir_numero_impar():
    respuesta = 0
    while True:
        respuesta = pedir_numero()
        if(respuesta % 2 == 0 or respuesta < 0):
            print("El numero ingresado no es impar o es negativo.")
        else:
            break
    return respuesta

def imprimir_marcador(j1,j2,sets1,sets2,juegos1,juegos2,puntos1,puntos2):
    print("\nJugador 1 (" + str(j1) + "):  Sets: " + str(sets1) + " | Juegos: " + str(juegos1) + " | Puntos: " + str(puntos1))
    print("Jugador 2 (" + str(j2) + "):  Sets: " + str(sets2) + " | Juegos: " + str(juegos2) + " | Puntos: " + str(puntos2))

def verificar_ganador(puntos1,puntos2):
    if puntos1 - puntos2 >= 2:
        return puntos1
    elif puntos2 - puntos1 >= 2:
        return puntos2
    else:
        return None
    
def mapear_puntos(puntos1,puntos2):
    puntos_tenis = {0:0,1:15,2:30,3:40,4:'Adv'}
    puntos_tenis1 = 0
    puntos_tenis2 = 0
    if (puntos1 <= 3 and puntos2 <= 3):
        puntos_tenis1 = puntos_tenis[puntos1]
        puntos_tenis2 = puntos_tenis[puntos2]
    elif (puntos1 == puntos2):
        puntos_tenis1 = puntos_tenis[3]
        puntos_tenis2 = puntos_tenis[3]
    elif (puntos1 > puntos2):
        puntos_tenis1 = puntos_tenis[4]
        puntos_tenis2 = puntos_tenis[3]
    else:
        puntos_tenis1 = puntos_tenis[3]
        puntos_tenis2 = puntos_tenis[4]
    
    return [puntos_tenis1,puntos_tenis2]
    

jugador1 = input("***Bienvenidos***\nIngrese el nombre del Jugador 1: ")
jugador2 = input("Ingrese el nombre del Jugador 2: ")

print("\n¿Cuantos sets se van a jugar? (Debe ser un numero impar)")
sets_a_jugar = pedir_numero_impar()
meta = (sets_a_jugar // 2) + 1

sets1 = sets2 = 0
sets_jugados = 0
while(not(sets1 == meta or sets2 == meta)):
    juegos1 = juegos2 = 0
    juegos_jugados = 1
    ganador_juegos = None
    
    while(ganador_juegos is None):
        puntos1 = puntos2 = 0
        ganador_puntos = None
        bandera = False
        print("\nJuego #" + str(juegos_jugados))
        if(juegos_jugados % 2 == 0):
            print("\nSaca el Jugador 1 (" + str(jugador1) + ")")
        else:
            print("\nSaca el Jugador 2 (" + str(jugador2) + ")")
            print("\nCambio de cancha")
        while(ganador_puntos is None):
            mapeados = mapear_puntos(puntos1,puntos2)
            puntos_t1 = mapeados[0]
            puntos_t2 = mapeados[1]
            imprimir_marcador(jugador1,jugador2,sets1,sets2,juegos1,juegos2,puntos_t1,puntos_t2)

            anotador = 0
            while(anotador == 0):
                print("\n¿Que jugador anota punto? (Ingese el numero de Jugador 1: " + str(jugador1) + " o Jugador 2: " + str(jugador2) + ")")
                anotador = pedir_numero()
                if(anotador == 1):
                    puntos1 += 1
                elif(anotador == 2):
                    puntos2 += 1
                else:
                    print("Opción invalida, trata de nuevo.")
                    anotador = 0

            if(puntos1 > 3 or puntos2 > 3):
                ganador_puntos = verificar_ganador(puntos1, puntos2)
        if (puntos1 > puntos2):
            print("\nEl jugador 1 (" + str(jugador1) + ") gano un juego!")
            juegos1 += 1
        else:
            print("\nEl jugador 2 (" + str(jugador2) + ") gano un juego!")
            juegos2 += 1

        if (juegos1 >= 6 or juegos2 >= 6):
            ganador_juegos = verificar_ganador(juegos1,juegos2)
        
        juegos_jugados += 1

    if (juegos1 > juegos2):
        print("\nEl jugador 1 (" + str(jugador1) + ") gano un set!")
        sets1 += 1
    else:
        print("\nEl jugador 2 (" + str(jugador2) + ") gano un set!")
        sets2 += 1

if (sets1 > sets2):
    print("\nEl jugador 1 (" + str(jugador1) + ") gano el partido!")
else:
    print("\nEl jugador 2 (" + str(jugador2) + ") gano el partido!")
def pedir_numero():
    entrada = -1
    while entrada == -1:
        try:
            entrada = int(input())
        except(ValueError):
            print("Lo ingresado no es un numero entero, ingresa el numero nuevamente.\n")
            entrada = -1
    
    return entrada



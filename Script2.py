def caminante(cadena):
    print("La cadena de entrada para el caminante es " + str(cadena))
    valles = 0
    altura_anterior = 0
    altura = 0
    for letra in cadena:
        if letra == 'D':
            altura_anterior = altura
            altura -= 1
        elif letra == 'U':
            altura_anterior = altura
            altura += 1

        if altura == 0 and altura_anterior < 0:
            valles += 1
            
    print("La cantidad de valles que el caminante recorrio es " + str(valles) + "\n")
    return valles

caminante("UUDDDUDDUDUUUDDU")
caminante("UUDUDUDUD")

class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.derecho = None
        self.izquierdo = None
    
class Arbol_binario_ordenado:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor <= nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecho)
    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.izquierdo)
        return self._buscar_recursivo(valor, nodo_actual.derecho)
        
    def recorrido_inorden(self):
        return self.recorrido_inorden_auxiliar(self.raiz)
    
    def recorrido_inorden_auxiliar(self, nodo_actual):
        if nodo_actual is not None:
            resultado_izquierdo = self.recorrido_inorden_auxiliar(nodo_actual.izquierdo)
            resultado_derecho = self.recorrido_inorden_auxiliar(nodo_actual.derecho)
            return resultado_izquierdo + [nodo_actual.valor] + resultado_derecho
        else:
            return []
        
    def recorrido_preorden(self):
        return self.recorrido_preorden_auxiliar(self.raiz)
    
    def recorrido_preorden_auxiliar(self, nodo_actual):
        if nodo_actual is not None:
            resultado_izquierdo = self.recorrido_preorden_auxiliar(nodo_actual.izquierdo)
            resultado_derecho = self.recorrido_preorden_auxiliar(nodo_actual.derecho)
            return  [nodo_actual.valor] + resultado_izquierdo + resultado_derecho
        else:
            return []

    def recorrido_postorden(self):
        return self.recorrido_postorden_auxiliar(self.raiz)
    
    def recorrido_postorden_auxiliar(self, nodo_actual):
        if nodo_actual is not None:
            resultado_izquierdo = self.recorrido_postorden_auxiliar(nodo_actual.izquierdo)
            resultado_derecho = self.recorrido_postorden_auxiliar(nodo_actual.derecho)
            return  resultado_izquierdo + resultado_derecho + [nodo_actual.valor]
        else:
            return []

mi_arbol = Arbol_binario_ordenado()
mi_arbol.insertar(3)
mi_arbol.insertar(2)
mi_arbol.insertar(3)
mi_arbol.insertar(1)
mi_arbol.insertar(5)
mi_arbol.insertar(4)
mi_arbol.insertar(7)
lista1 = mi_arbol.recorrido_inorden()
print(lista1)
lista2 = mi_arbol.recorrido_preorden()
print(lista2)
lista3 = mi_arbol.recorrido_postorden()
print(lista3)
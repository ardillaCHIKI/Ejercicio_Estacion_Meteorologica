class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sublista = Lista()  # sublista para datos climáticos
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

def insertar(lista, dato):
    nodo = Nodo(dato)
    if lista.cabeza is None:
        lista.cabeza = nodo
    else:
        actual = lista.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo

def buscar(lista, dato):
    actual = lista.cabeza
    while actual:
        if actual.dato == dato:
            return actual
        actual = actual.siguiente
    return None

def barrido(lista):
    actual = lista.cabeza
    while actual:
        print(f" - {actual.dato}")
        actual = actual.siguiente
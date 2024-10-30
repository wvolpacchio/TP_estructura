class NodoContacto:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.siguiente = None

class Contactos:
    def __init__(self):
        self.cabeza = None

    def agendar_contacto(self, nombre, numero):
        nuevo_contacto = NodoContacto(nombre, numero)
        if not self.cabeza:
            self.cabeza = nuevo_contacto
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_contacto
        print(f'Contacto {nombre} agendado con éxito.')

    def actualizar_contacto(self, nombre, nuevo_numero):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                actual.numero = nuevo_numero
                print(f'Número de {nombre} actualizado a {nuevo_numero}.')
                return
            actual = actual.siguiente
        print(f'Contacto {nombre} no encontrado.')

    def mostrar_contactos(self):
        if not self.cabeza:
            print("La lista de contactos está vacía.")
        else:
            actual = self.cabeza
            while actual:
                print(f'Nombre: {actual.nombre}, Número: {actual.numero}')
                actual = actual.siguiente

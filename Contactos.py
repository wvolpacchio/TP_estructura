class Contactos:
    def __init__(self):
        self.lista_contactos = []

    def agendar_contacto(self, nombre, numero):
        self.lista_contactos.append({"nombre": nombre, "numero": numero})
        print(f'Contacto {nombre} agendado con exito.')

    def actualizar_contacto(self, nombre, nuevo_numero):
        for contacto in self.lista_contactos:
            if contacto["nombre"] == nombre:
                contacto["numero"] = nuevo_numero
                print(f'Numero de {nombre} actualizado a {nuevo_numero}.')
                return
        print(f'Contacto {nombre} no encontrado.')

    def mostrar_contactos(self):
        if not self.lista_contactos:
            print("La lista de contactos esta vacia.")
        else:
            for contacto in self.lista_contactos:
                print(f'Nombre: {contacto["nombre"]}, Numero: {contacto["numero"]}')

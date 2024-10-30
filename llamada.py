class Llamada:
    def __init__(self, numero_destino, numero_origen):
        self.numero_destino = numero_destino
        self.numero_origen = numero_origen
        self.en_llamada = True

    def terminar_llamada(self):
        self.en_llamada = False
        print("La llamada ha terminado.")


class HistorialLlamadas:
    def __init__(self):
        self.pila_llamadas = []  # Pila para almacenar llamadas

    def realizar_llamada(self, numero_destino, numero_origen):
        llamada = Llamada(numero_destino, numero_origen)
        self.pila_llamadas.append(llamada)
        print(f'Realizando llamada al numero {numero_destino} desde el numero {numero_origen}.')

    def terminar_llamada(self):
        if self.pila_llamadas:
            llamada = self.pila_llamadas.pop()  # Sacar la ultima llamada de la pila
            llamada.terminar_llamada()  # Llamar al metodo de la instancia de la llamada
        else:
            print("No hay llamadas en curso.")

    def mostrar_historial(self):
        if not self.pila_llamadas:
            print("El historial de llamadas esta vacio.")
        else:
            print("Historial de Llamadas (ultima llamada primero):")
            for llamada in reversed(self.pila_llamadas):  # Mostrar en orden de ultimo a primero
                estado = "En llamada" if llamada.en_llamada else "Terminada"  # Acceder al atributo de la instancia
                print(f"Numero: {llamada.numero_destino}, Estado: {estado}")


# Crear una instancia del historial de llamadas
historial = HistorialLlamadas()

# Realizar una llamada
historial.realizar_llamada("123456789", "987654321")

# Terminar la ultima llamada
historial.terminar_llamada()

# Mostrar el historial de llamadas
historial.mostrar_historial()

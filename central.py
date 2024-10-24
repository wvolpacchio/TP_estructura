from telefono import Telefono 

class Central:
    def __init__(self):
        self.dispositivos_registrados = {}  # Almacena los dispositivos con su numero de telefono como clave
        self.logs = []  # Almacena los logs de las comunicaciones

    def registrar_dispositivo(self, telefono):
        """Registra un telefono en la central"""
        if telefono.numero not in self.dispositivos_registrados:
            self.dispositivos_registrados[telefono.numero] = telefono
            print(f"Telefono {telefono.numero} registrado en la central.")
        else:
            print(f"El telefono {telefono.numero} ya esta registrado.")

    def eliminar_dispositivo(self, telefono):
        """Elimina un telefono de la central"""
        if telefono.numero in self.dispositivos_registrados:
            del self.dispositivos_registrados[telefono.numero]
            print(f"Telefono {telefono.numero} eliminado de la central.")
        else:
            print(f"El telefono {telefono.numero} no esta registrado.")

    def verificar_disponibilidad(self, numero):
        """Verifica si un telefono esta disponible en la red"""
        if numero in self.dispositivos_registrados:
            telefono = self.dispositivos_registrados[numero]
            if telefono.encendido and telefono.red_movil:
                print(f"Telefono {numero} disponible para comunicacion.")
                return True
            else:
                print(f"Telefono {numero} no disponible (apagado o sin red movil).")
                return False
        else:
            print(f"Telefono {numero} no esta registrado en la red.")
            return False

    def establecer_comunicacion(self, origen, destino):
        """Establece una comunicacion entre dos dispositivos"""
        if self.verificar_disponibilidad(origen) and self.verificar_disponibilidad(destino):
            print(f"Comunicacion establecida entre {origen} y {destino}.")
            self.registrar_log(f"Llamada entre {origen} y {destino}.")
        else:
            print("No se puede establecer la comunicacion.")

    def gestionar_llamadas(self):
        """Gestiona el estado de las llamadas (ocupado, finalizar)"""
        print("Gestionando llamadas...")
        # Aqui podrias implementar mas logica como llamadas en curso, finalizacion, etc.

    def verificar_acceso_internet(self, numero):
        """Verifica si un telefono tiene acceso a internet"""
        if numero in self.dispositivos_registrados:
            telefono = self.dispositivos_registrados[numero]
            if telefono.encendido and telefono.datos_movil:
                print(f"Telefono {numero} tiene acceso a internet.")
                return True
            else:
                print(f"Telefono {numero} no tiene acceso a internet.")
                return False
        else:
            print(f"Telefono {numero} no esta registrado en la red.")
            return False

    def registrar_log(self, info_comunicacion):
        """Registra un log de las comunicaciones"""
        self.logs.append(info_comunicacion)
        print(f"Log registrado: {info_comunicacion}")

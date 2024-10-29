import csv
from datetime import datetime
from telefono import Telefono

class Central:
    def __init__(self):
        self.dispositivos_registrados = {}
        self.logs = []

    def registrar_dispositivo(self, telefono):
        """Registra un telefono en la central si no esta registrado."""
        if telefono.num_telefono not in self.dispositivos_registrados:
            self.dispositivos_registrados[telefono.num_telefono] = telefono
            print(f"Telefono {telefono.num_telefono} registrado en la central.")
            self.registrar_log("Registro", f"Telefono {telefono.num_telefono} registrado.", "Exito")
        else:
            print(f"El telefono {telefono.num_telefono} ya esta registrado.")
            self.registrar_log("Registro", f"Intento de registro duplicado para el telefono {telefono.num_telefono}.", "Fallo")

    def eliminar_dispositivo(self, telefono):
        """Elimina un telefono de la central si esta registrado."""
        if telefono.num_telefono in self.dispositivos_registrados:
            del self.dispositivos_registrados[telefono.num_telefono]
            print(f"Telefono {telefono.num_telefono} eliminado de la central.")
            self.registrar_log("Baja", f"Telefono {telefono.num_telefono} eliminado.", "Exito")
        else:
            print(f"El telefono {telefono.num_telefono} no esta registrado.")
            self.registrar_log("Baja", f"Intento de baja para un telefono no registrado {telefono.num_telefono}.", "Fallo")

    def actualizar_estado_dispositivo(self, telefono, estado="Disponible"):
        """Actualiza el estado de disponibilidad del dispositivo en la red."""
        if telefono.num_telefono in self.dispositivos_registrados:
            self.registrar_log("Estado", f"Estado actualizado para {telefono.num_telefono}: {estado}", "Exito")
            print(f"Estado del dispositivo {telefono.num_telefono}: {estado}")

    def verificar_disponibilidad(self, numero):
        """Verifica si un telefono esta disponible en la red."""
        if numero in self.dispositivos_registrados:
            telefono = self.dispositivos_registrados[numero]
            if telefono.encendido and telefono.configuracion.red_movil_activa and not telefono.en_llamada:
                return True
        return False

    def verificar_acceso_internet(self, numero):
        """Verifica si el dispositivo tiene datos moviles activos y esta encendido."""
        if numero in self.dispositivos_registrados:
            telefono = self.dispositivos_registrados[numero]
            if telefono.encendido and telefono.configuracion.datos_movil_activos:
                return True
        return False

    def establecer_comunicacion(self, origen, destino, tipo, mensaje=""):
        """
        Establece una comunicacion entre dos dispositivos si ambos estan disponibles.
        Registra el tipo de operacion (llamada, SMS, etc.) y el mensaje si corresponde.
        """
        if self.verificar_disponibilidad(origen) and self.verificar_disponibilidad(destino):
            self.registrar_log(tipo, f"Comunicacion establecida entre {origen} y {destino}: {mensaje}", "Exito")
            print(f"{tipo} establecida entre {origen} y {destino}.")
            self.actualizar_estado_dispositivo(self.dispositivos_registrados[origen], "Ocupado")
            self.actualizar_estado_dispositivo(self.dispositivos_registrados[destino], "Ocupado")
        else:
            print("No se puede establecer la comunicacion. Ambos dispositivos deben estar disponibles.")
            self.registrar_log(tipo, f"Fallo en comunicacion entre {origen} y {destino}. Estado de disponibilidad fallo.", "Fallo")

    def terminar_comunicacion(self, telefono):
        """Finaliza la comunicacion y actualiza el estado del dispositivo a disponible."""
        if telefono.num_telefono in self.dispositivos_registrados:
            self.actualizar_estado_dispositivo(telefono, "Disponible")

    def registrar_log(self, tipo, info_comunicacion, estado):
        """Registra un log detallado de las comunicaciones en un archivo CSV y en la lista de logs."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {tipo} - {info_comunicacion} - Estado: {estado}"
        self.logs.append(log_entry)
        print(f"Log registrado: {log_entry}")
        with open("logs_comunicaciones.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, tipo, info_comunicacion, estado])

    def mostrar_logs(self):
        """Muestra todos los logs registrados en la consola."""
        if not self.logs:
            print("No hay logs registrados.")
        for log in self.logs:
            print(log)
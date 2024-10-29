import csv
from datetime import datetime

class Central:
    def __init__(self):
        self.dispositivos_registrados = {}
        self.logs = []

    def registrar_dispositivo(self, telefono):
        if telefono.num_telefono not in self.dispositivos_registrados:
            self.dispositivos_registrados[telefono.num_telefono] = telefono
            print(f"Teléfono {telefono.num_telefono} registrado en la central.")
            self.registrar_log("Registro", f"Teléfono {telefono.num_telefono} registrado.", "Éxito")
        else:
            print(f"El teléfono {telefono.num_telefono} ya está registrado.")
            self.registrar_log("Registro", f"Intento de registro duplicado para el teléfono {telefono.num_telefono}.", "Fallo")

    def eliminar_dispositivo(self, telefono):
        if telefono.num_telefono in self.dispositivos_registrados:
            del self.dispositivos_registrados[telefono.num_telefono]
            print(f"Teléfono {telefono.num_telefono} eliminado de la central.")
            self.registrar_log("Baja", f"Teléfono {telefono.num_telefono} eliminado.", "Éxito")
        else:
            print(f"El teléfono {telefono.num_telefono} no está registrado.")
            self.registrar_log("Baja", f"Intento de baja para un teléfono no registrado {telefono.num_telefono}.", "Fallo")

    def actualizar_estado_dispositivo(self, telefono, estado="Disponible"):
        """Actualiza la disponibilidad del dispositivo en la red según su estado actual."""
        if telefono.num_telefono in self.dispositivos_registrados:
            self.registrar_log("Estado", f"Estado actualizado para {telefono.num_telefono}: {estado}", "Éxito")
            print(f"Estado del dispositivo {telefono.num_telefono}: {estado}")

    def verificar_disponibilidad(self, numero):
        if numero in self.dispositivos_registrados:
            telefono = self.dispositivos_registrados[numero]
            if telefono.encendido and telefono.configuracion.red_movil_activa and not telefono.en_llamada:
                return True
        return False

    def verificar_acceso_internet(self, numero):
        """Verifica si el dispositivo tiene datos móviles activos y está encendido."""
        if numero in self.dispositivos_registrados:
            telefono = self.dispositivos_registrados[numero]
            if telefono.encendido and telefono.configuracion.datos_movil_activos:
                return True
        return False

    def establecer_comunicacion(self, origen, destino, tipo, mensaje=""):
        if self.verificar_disponibilidad(origen) and self.verificar_disponibilidad(destino):
            self.registrar_log(tipo, f"Comunicación establecida entre {origen} y {destino}: {mensaje}", "Éxito")
            print(f"{tipo} establecida entre {origen} y {destino}.")
            self.actualizar_estado_dispositivo(self.dispositivos_registrados[origen], "Ocupado")
            self.actualizar_estado_dispositivo(self.dispositivos_registrados[destino], "Ocupado")
        else:
            print("No se puede establecer la comunicación. Ambos dispositivos deben estar disponibles.")
            self.registrar_log(tipo, f"Fallo en comunicación entre {origen} y {destino}. Estado de disponibilidad falló.", "Fallo")

    def terminar_comunicacion(self, telefono):
        if telefono.num_telefono in self.dispositivos_registrados:
            self.actualizar_estado_dispositivo(telefono, "Disponible")

    def registrar_log(self, tipo, info_comunicacion, estado):
        """Registra un log detallado de las comunicaciones."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {tipo} - {info_comunicacion} - Estado: {estado}"
        self.logs.append(log_entry)
        print(f"Log registrado: {log_entry}")
        with open("logs_comunicaciones.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, tipo, info_comunicacion, estado])

    def mostrar_logs(self):
        """Imprime los logs registrados en consola."""
        if not self.logs:
            print("No hay logs registrados.")
        for log in self.logs:
            print(log)

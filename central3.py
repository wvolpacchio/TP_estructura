import csv
from datetime import datetime

class Central:
    def __init__(self):
        self.dispositivos_registrados = {}
        self.logs = []

    def registrar_dispositivo(self, telefono):
        if telefono.encendido:
            if telefono.num_telefono not in self.dispositivos_registrados:
                self.dispositivos_registrados[telefono.num_telefono] = telefono
                print(f"Teléfono {telefono.num_telefono} registrado en la central.")
                self.registrar_log("Registro", f"Teléfono {telefono.num_telefono} registrado.")
            else:
                print(f"El teléfono {telefono.num_telefono} ya está registrado.")
        else:
            print("El teléfono debe estar encendido para registrarse en la central.")

    def eliminar_dispositivo(self, telefono):
        if telefono.num_telefono in self.dispositivos_registrados:
            del self.dispositivos_registrados[telefono.num_telefono]
            print(f"Teléfono {telefono.num_telefono} eliminado de la central.")
            self.registrar_log("Baja", f"Teléfono {telefono.num_telefono} eliminado.")
        else:
            print(f"El teléfono {telefono.num_telefono} no está registrado.")

    def actualizar_estado_dispositivo(self, telefono, estado="Disponible"):
        """Actualiza la disponibilidad del dispositivo en la red según su estado actual."""
        if telefono.encendido:
            if telefono.num_telefono in self.dispositivos_registrados:
                self.registrar_log("Estado", f"Estado actualizado para {telefono.num_telefono}: {estado}")
                print(f"Estado del dispositivo {telefono.num_telefono}: {estado}")
        else:
            print("El dispositivo debe estar encendido para actualizar su estado.")

    def establecer_comunicacion(self, origen, destino, tipo, mensaje=""):
        if origen in self.dispositivos_registrados and destino in self.dispositivos_registrados:
            origen_telefono = self.dispositivos_registrados[origen]
            destino_telefono = self.dispositivos_registrados[destino]
            if origen_telefono.encendido and destino_telefono.encendido:
                self.registrar_log(tipo, f"Comunicación establecida entre {origen} y {destino}: {mensaje}")
                print(f"{tipo} establecida entre {origen} y {destino}.")
                self.actualizar_estado_dispositivo(origen_telefono, "Ocupado")
                self.actualizar_estado_dispositivo(destino_telefono, "Ocupado")
            else:
                print("Ambos dispositivos deben estar encendidos para establecer comunicación.")
                self.registrar_log("Error", f"Fallo en comunicación entre {origen} y {destino}. Estado de disponibilidad falló.")
        else:
            print("Ambos dispositivos deben estar registrados para establecer comunicación.")

    def registrar_log(self, tipo, info_comunicacion):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {tipo} - {info_comunicacion}"
        self.logs.append(log_entry)
        print(f"Log registrado: {log_entry}")
        with open("logs_comunicaciones.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, tipo, info_comunicacion])

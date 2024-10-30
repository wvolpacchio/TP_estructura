from datetime import datetime
from collections import deque

class SMS:
    def __init__(self):
        self.historial_sms = deque()  # Cola para almacenar mensajes en orden de llegada.

    def enviar_sms(self, numero_origen, numero_destino, mensaje):
        """Envia un SMS y lo agrega al historial."""
        sms = {
            'numero_origen': numero_origen,
            'numero_destino': numero_destino,
            'mensaje': mensaje,
            'fecha': datetime.now(),
            'leido': True
        }
        self.historial_sms.append(sms)
        print(f"Enviando SMS de {numero_origen} a {numero_destino}: {mensaje}")

    def recibir_sms(self, numero_origen, numero_destino, mensaje):
        """Recibe un SMS y lo agrega al historial."""
        sms = {
            'numero_origen': numero_origen,
            'numero_destino': numero_destino,
            'mensaje': mensaje,
            'fecha': datetime.now(),
            'leido': False
        }
        self.historial_sms.append(sms)
        print(f"Recibido SMS de {numero_origen} a {numero_destino}: {mensaje}")

    def ver_historial_sms(self):
        """Muestra el historial completo de SMS, ordenado por fecha de llegada."""
        if not self.historial_sms:
            print("No hay SMS en el historial.")
            return

        for sms in self.historial_sms:
            estado = "Leido" if sms['leido'] else "No leido"
            print(f"Fecha: {sms['fecha']}, Origen: {sms['numero_origen']}, Destino: {sms['numero_destino']}, Estado: {estado}")
            print(f"Mensaje: {sms['mensaje']}\n")
            
    def eliminar_sms(self):
        """Elimina el SMS más antiguo del historial."""
        if self.historial_sms:
            eliminado = self.historial_sms.popleft()  # Elimina del frente de la cola
            print(f'SMS de {eliminado["numero_origen"]} a {eliminado["numero_destino"]} eliminado.')
        else:
            print("No hay SMS para eliminar.")
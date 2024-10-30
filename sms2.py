class SMS:
    def __init__(self, telefono):
        self.telefono = telefono
        self.bandeja_entrada = []  # Bandeja de mensajes recibidos
        self.bandeja_enviados = []  # Bandeja de mensajes enviados
    
    # Enviar SMS a otro numero
    def enviar_sms(self, num_destino, mensaje):
        sms = {"num_destino": num_destino, "mensaje": mensaje, "estado": "Enviado"}
        self.bandeja_enviados.append(sms)
        print(f"Mensaje enviado a {num_destino}: {mensaje}")

    # Recibir un SMS
    def recibir_sms(self, num_origen, mensaje):
        sms = {"num_origen": num_origen, "mensaje": mensaje, "estado": "No leido"}
        self.bandeja_entrada.append(sms)
        print(f"Mensaje recibido de {num_origen}: {mensaje}")

    # Ver mensajes no leidos primero
    def ver_bandeja_entrada(self):
        mensajes_no_leidos = [sms for sms in self.bandeja_entrada if sms["estado"] == "No leido"]
        for sms in mensajes_no_leidos:
            print(f"De {sms['num_origen']}: {sms['mensaje']}")
            sms["estado"] = "Leido"
        
        mensajes_leidos = [sms for sms in self.bandeja_entrada if sms["estado"] == "Leido"]
        for sms in mensajes_leidos:
            print(f"De {sms['num_origen']}: {sms['mensaje']} (Leido)")

    # Eliminar mensajes de la bandeja de entrada
    def eliminar_sms(self, num_origen=None):
        if num_origen:
            self.bandeja_entrada = [sms for sms in self.bandeja_entrada if sms["num_origen"] != num_origen]
            print(f"Mensajes de {num_origen} eliminados.")
        else:
            self.bandeja_entrada.clear()
            print("Todos los mensajes eliminados.")

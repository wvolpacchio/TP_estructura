class SMS:
    def __init__(self, numero_origen, numero_destino, mensaje):
        self.numero_origen = numero_origen
        self.numero_destino = numero_destino
        self.mensaje = mensaje
        self.fecha = None  # Aqui puedes agregar la logica para establecer la fecha
        self.leido = False
    def enviar(self):
       
        print(f"Enviando SMS de {self.numero_origen} a {self.numero_destino}: {self.mensaje}")

    def recibir(self, mensaje, numero_origen):
        
        self.mensaje = mensaje
        self.numero_origen = numero_origen
        self.leido = False
        print(f"Recibido SMS de {self.numero_origen}: {self.mensaje}")

    def listar_sms(self):
        
        print(f"Mensaje de {self.numero_origen}: {self.mensaje} - Leido: {self.leido}")
    
    def eliminar_sms(self):
        
        print(f"Eliminando SMS de {self.numero_origen}: {self.mensaje}")
       

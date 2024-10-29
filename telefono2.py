from configuracion import Configuracion
from contactos import Contactos
from central import Central
from llamada import Llamada
from sms import SMS
from email import Email
from app_store import AppStore

class Telefono:
    dic_aplicaciones = {}

    def __init__(self, id, nombre, modelo, sistema_operativo, sistema_operativo_version, RAM, cap_almacenamiento, num_telefono, codigo_desbloqueo):
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.sistema_operativo_version = sistema_operativo_version
        self.RAM = RAM
        self.num_telefono = self.validar_numero(num_telefono)
        self.cap_almacenamiento = cap_almacenamiento
        self.encendido = False
        self.bloqueado = True
        self.codigo_desbloqueo = codigo_desbloqueo
        self.configuracion = Configuracion(nombre, codigo_desbloqueo)
        self.contactos = Contactos()
        self.central = Central()  
        self.llamadas = []  
        self.sms_bandeja = []  
        self.email = Email()
        self.app_store = AppStore()  

    def validar_numero(self, num_telefono):
        if 1000000000 <= num_telefono <= 9999999999:
            return num_telefono
        else:
            raise ValueError("El número de teléfono debe tener exactamente 10 dígitos.")

    def encender(self):
        if not self.encendido:
            self.encendido = True
            self.configuracion.red_movil_activa = True
            self.central.registrar_dispositivo(self)
            print(f"{self.nombre} encendido y registrado en la central.")
        else:
            print(f"{self.nombre} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.bloqueado = True
            self.configuracion.red_movil_activa = False
            print(f"{self.nombre} apagado.")
        else:
            print(f"{self.nombre} ya está apagado.")

    def bloquear(self):
        if self.encendido and not self.bloqueado:
            self.bloqueado = True
            print(f"{self.nombre} bloqueado.")
        elif not self.encendido:
            print("El teléfono está apagado, no se puede bloquear.")
        else:
            print(f"{self.nombre} ya está bloqueado.")

    def desbloquear(self):
        if self.encendido and self.bloqueado:
            codigo = input("Ingrese el código de desbloqueo: ")
            if codigo == self.codigo_desbloqueo:
                self.bloqueado = False
                print(f"{self.nombre} desbloqueado.")
            else:
                print("Código incorrecto.")
        elif not self.encendido:
            print("El teléfono está apagado, no se puede desbloquear.")
        else:
            print(f"{self.nombre} ya está desbloqueado.")

    def abrir_aplicacion(self, app_nombre):
        if self.encendido and not self.bloqueado:
            if app_nombre in self.dic_aplicaciones:
                app = self.dic_aplicaciones[app_nombre]
                app.abrir()
            else:
                print(f"La aplicación {app_nombre} no está instalada.")
        else:
            print("El teléfono debe estar encendido y desbloqueado para abrir una aplicación.")

    def realizar_llamada(self, numero_destino):
        if self.encendido and not self.bloqueado:
            llamada = Llamada()
            llamada.realizar_llamada(numero_destino)
            self.llamadas.append(llamada)
            self.central.establecer_comunicacion(self.num_telefono, numero_destino, "Llamada")
        else:
            print("El teléfono debe estar encendido y desbloqueado para realizar una llamada.")

    def enviar_sms(self, numero_destino, mensaje):
        if self.encendido and not self.bloqueado:
            sms = SMS(self.num_telefono, numero_destino, mensaje)
            sms.enviar()
            self.sms_bandeja.append(sms)
            self.central.establecer_comunicacion(self.num_telefono, numero_destino, "SMS", mensaje)
        else:
            print("El teléfono debe estar encendido y desbloqueado para enviar un SMS.")
    
    def mostrar_historial_llamadas(self):
        if self.encendido:
            if self.llamadas:
                for llamada in self.llamadas:
                    print(f"Llamada a {llamada.numero_destino} - En llamada: {llamada.en_llamada}")
            else:
                print("No hay historial de llamadas.")
        else:
            print("El teléfono debe estar encendido para ver el historial de llamadas.")

    def ver_bandeja_sms(self):
        if self.encendido:
            if self.sms_bandeja:
                for sms in self.sms_bandeja:
                    sms.listar_sms()
            else:
                print("La bandeja de SMS está vacía.")
        else:
            print("El teléfono debe estar encendido para ver la bandeja de SMS.")

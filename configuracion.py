

class Configuracion:
    def __init__(self, nombre_dispositivo, codigo_desbloqueo):
        self.nombre_dispositivo = nombre_dispositivo
        self.codigo_desbloqueo = codigo_desbloqueo
        self.red_movil_activa = False
        self.datos_movil_activos = False

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre_dispositivo = nuevo_nombre
        print(f'Nombre del dispositivo cambiado a: {nuevo_nombre}')

    def cambiar_codigo_desbloqueo(self, nuevo_codigo):
        self.codigo_desbloqueo = nuevo_codigo
        print('Codigo de desbloqueo cambiado exitosamente.')

    def cambiar_red_movil(self):
        self.red_movil_activa = not self.red_movil_activa

    def cambiar_datos_moviles(self):
        self.datos_movil_activos = not self.datos_movil_activos
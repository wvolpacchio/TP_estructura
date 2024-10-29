
class Configuracion():
    def __init__(self, nombre_dispositivo, codigo_desbloqueo):
        self.nombre_dispositivo = nombre_dispositivo
        self.codigo_desbloqueo = codigo_desbloqueo
        self.red_movil_activa = False  #Inicialmente red movil activada
        self.datos_movil_activos = False  #inicialmente datos moviles activado

    #Cambia el nombre del telefono a un nuevo nombre
    def cambiar_nombre(self):
        nuevo_nombre = input("Ingrese nuevo nombre para el dispositivo")
        self.nombre_dispositivo = nuevo_nombre
        print(f'Nombre del dispositivo cambiado a: {nuevo_nombre}')

    #Modifica el codigo de desbloqueo del telefono
    def cambiar_codigo_desbloqueo(self):
        nuevo_codigo = ("Ingrese nuevo codigo para el dispositivo")
        self.codigo_desbloqueo = nuevo_codigo
        print('Codigo de desbloqueo cambiado exitosamente.')

    #Alterna el estado de la red movil entre activado y desactivado
    def alternar_red_movil(self):
        self.red_movil_activa = not self.red_movil_activa
        if self.red_movil_activa:
            estado = "activada" 
        else: 
            estado ="desactivada"
        print(f"Red movil {estado}.")

    #Alterna el estado de los datos moviles entre activado y desactivado
    def alternar_datos_moviles(self):
        self.datos_movil_activos = not self.datos_movil_activos
        if self.datos_movil_activos:
            estado = "activados" 
        else:
            estado = "desactivados"
        print(f"Datos moviles {estado}.")
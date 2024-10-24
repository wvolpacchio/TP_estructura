from configuracion import Configuracion

class Telefono():
    dic_aplicaciones = {}

    def __init__(self, id, nombre, modelo, sistema_operativo, version, RAM, cap_almacenamiento, num_telefono:int, codigo_desbloqueo:str):
        self.id = id 
        self.nombre = nombre 
        self.modelo = modelo 
        self.sistema_operativo = sistema_operativo
        self.version = version 
        self.RAM = RAM 
        self.num_telefono = self.validar_numero(num_telefono)
        self.cap_almacenamiento = cap_almacenamiento
        self.encendido = False
        self.bloqueado = True
        self.disponibilidad = "No disponible"
        self.red_movil = False
        self.datos_moviles = False
        self.codigo_desbloqueo = codigo_desbloqueo
        self.configuracion = Configuracion()

    # Asegurar que tenga exactamente 10 digitos    
    def validar_numero(self, num_telefono):
        # Contar el numero de digitos
        if 1000000000 <= num_telefono <= 9999999999:  # Rango de un numero de 10 digitos
            return num_telefono
        else:
            raise ValueError("El numero de telefono no es valido. Debe tener exactamente 10 digitos.")

    def disponibilidad_telefono(self): 
        if self.red_movil and self.datos_moviles:
            self.disponibilidad = "Disponible"
        else:
            self.disponibilidad = "No disponible"
        
    # Funcion para apagar el telefono
    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.red_movil = False #Se apaga la red movil al apagar el telefono
            print(f'{self.nombre} apagado.')
        else:
            print(f'{self.nombre} ya esta apagado.')

    # Funcion para prender el telefono
    def prender(self):
        if not self.encendido:
            self.encendido = True
            print(f'{self.nombre} encendido.')
            self.activar_red_movil()  # Activar la red movil automaticamente al encender
        else:
            print(f'{self.nombre} ya esta encendido.') 
    
    # Funcion para bloquear el telefono
    def bloquear(self): 
        if self.encendido and not self.bloqueado:
            self.bloqueado = True
            print(f"El telefono {self.nombre} esta bloqueado.")
        elif not self.encendido:
            print(f"El telefono {self.nombre} este apagado. No se puede bloquear.")
        else:
            print(f"El telefono {self.nombre} ya esta bloqueado.")

    # Funcion para desbloquear el telefono
    def desbloquear(self):
        if self.encendido and self.bloqueado:
            codigo = int(input("Ingresa el codigo de desbloqueo: "))
            if codigo == self.codigo_desbloqueo:
                self.bloqueado = False
                print(f"El telefono {self.nombre} esta desbloqueado.")
            else:
                print("Codigo de desbloqueo incorrecto.")
        elif not self.encendido:
            print(f"El telefono {self.nombre} esta apagado. No se puede desbloquear.")
        else:
            print(f"El telefono {self.nombre} ya esta desbloqueado.")

    # Cambiar la red movil al encender el telefono
    def cambiar_red_movil(self):
        print("Red movil cambiada.")
        self.configuracion.cambiar_red_movil()

    # Desactivar la red movil
    def desactivar_red_movil(self):
        if self.red_movil:
            self.red_movil = False
            print("Red movil desactivada.")
        else:
            print("La red movil ya esta desactivada.")

    # Activar los datos moviles (conectividad a internet)
    def activar_datos_moviles(self):
        if self.red_movil:
            self.datos_moviles = True
            print("Datos moviles activados.")
        else:
            print("No se puede activar los datos moviles sin red movil.")

    # Desactivar los datos moviles
    def desactivar_datos_moviles(self):
        if self.datos_moviles:
            self.datos_moviles = False
            print("Datos moviles desactivados.")
        else:
            print("Los datos moviles ya estan desactivados.")    

    # Cambiar el nombre del telefono
    def cambiar_nombre(self):
        nuevo_nombre = input("Ingresa el nuevo nombre para el telefono: ")
        self.nombre = nuevo_nombre
        print(f"El nombre del telefono ha sido cambiado a {self.nombre}.")
    
    def cambiar_codigo_desbloqueo(self):
       nuevo_codigo=str(input("Ingresa el nuevo codigo de desbloqueo: "))
       if nuevo_codigo==self.codigo_desbloqueo:
           print("El codigo ya existe")
       else:
           self.codigo_desbloqueo=nuevo_codigo
           print("El nuevo codigo es {nuevo_codigo}")
       
    def __str__(self):
        return (f'Telefono #{self.id}, Nombre: {self.nombre}, Modelo: {self.modelo}, '
                f'Sistema Operativo: {self.sistema_operativo}, Version: {self.version}, '
                f'RAM: {self.RAM}, Capacidad Almacenamiento: {self.cap_almacenamiento}, '
                f'Numero Telefono: {self.num_telefono}')
             

# Prueba de configuración
try:
    telefono = Telefono(1, "Carlos", "Motorola", "Android", "10", 8, 500, 1149157657, "hola123")
    telefono.prender()  # Se enciende y automáticamente activa la red móvil
    telefono.activar_datos_moviles()  # Activa los datos móviles
    print(telefono)  # Imprime el estado del teléfono

    # Cambiar nombre del teléfono
    telefono.cambiar_nombre()

    # Cambiar el código de desbloqueo
    telefono.cambiar_codigo_desbloqueo()

    # Intentar desbloquear el teléfono
    telefono.desbloquear()

    # Desactivar los datos móviles
    telefono.desactivar_datos_moviles()

    # Desactivar la red móvil
    telefono.desactivar_red_movil()

    # Apagar el teléfono
    telefono.apagar()
except ValueError as e:
    print(e)

    
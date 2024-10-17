class Telefono():
    dic_telefonos = {}
    def __init__(self, id, nombre, modelo, sistema_operativo, version, RAM, cap_almacenamiento, num_telefono):
        self.id = id 
        self.nombre = nombre 
        self.modelo = modelo 
        self.sistema_operativo = sistema_operativo
        self.version = version 
        self.RAM = RAM 
        self.num_telefono = num_telefono
        self.cap_almacenamiento = cap_almacenamiento
        self.encendido = False
        self.bloqueado = True


        if Telefono.telefono_ya_registrado(id):
            raise ValueError(f'Error: Telefono {id} ya esta registrada')
        Telefono.dic_telefonos[id]=self


        
    @staticmethod
    def telefono_ya_registrado(id):
        return id in Telefono.dic_telefonos.keys()
    
    # def llamadas_telefono():
    #     if 
    
    
    def __str__(self) -> str:
        return f'''Telefono #{self.id}, Nombre: {self.nombre}, Modelo: {self.modelo}, Sistema Operativo: {self.sistema_operativo}, Version: {self.version}, RAM: {self.RAM}, Capacidad Almacenamiento: {self.cap_almacenamiento}, Numero Telefono: {self.num_telefono}'''
    
    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f'{self.nombre} se apago el telefono.')
        else:
            print(f'{self.nombre} ya esta apagado.')

    def prender(self):
        if not self.encendido:
            self.encendido = True
            print(f'{self.nombre} se prendio el telefono.')
        else:
            print(f'{self.nombre} ya esta prendido.') 
    
    def bloquear (self): 
        if self.bloqueado: 
            self.bloqueado = True
            print(f'{self.nombre} se bloqueo.')
        else:
            print(f'{self.nombre} ya esta bloqueado.') 

    def desbloquear (self): 
        if self.bloqueado: 
            self.bloqueado = False
            print(f'{self.nombre} se desbloqueo.')
        else:
            print(f'{self.nombre} ya esta desbloqueado.') 
            


            
from telefono import Telefono

class Central():
    dic_telefonos = {}
    def __init__(self,dato):
        self.dato=dato 
        
      
    @staticmethod
    def telefono_ya_registrado(id):
        return id in Telefono.dic_telefonos.keys()
    
    def __str__(self) -> str:
            return f'''Telefono #{self.id}, Nombre: {self.nombre}, Modelo: {self.modelo}, Sistema Operativo: {self.sistema_operativo}'''

    @staticmethod
    def registrar_telefono(id):
        if id in Central.dic_telefonos:
             return f'El telefono #{id} ya se encuentra en la central'
        else:
            Central.dic_telefonos.add(id)
            return f'El telefono #{id} se agrego correctamente a la central'

    @staticmethod   
    def baja_telefono(id):
        if id in Central.dic_telefonos:
            Central.dic_telefonos.remove(id)
            return f'El telefono #{id} fue eliminado de la central'
        else:
            return f'El telefono #{id} no se encuentra en la central'
    
    
        

            
class Aplicacion:
    def __init__(self, nombre, version, categoria):
        self.nombre = nombre
        self.version = version
        self.categoria = categoria

    def abrir(self):
        print(f'Abriendo la aplicacion: {self.nombre}')

    def actualizar(self, nueva_version):
        self.version = nueva_version
        print(f'Aplicacion {self.nombre} actualizada a la version: {nueva_version}')

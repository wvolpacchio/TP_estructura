class AppStore:
    def __init__(self):
        self.aplicaciones = []

    def buscar_app(self, nombre_app):
        for app in self.aplicaciones:
            if app['nombre'] == nombre_app:
                print(f'Aplicacion encontrada: {app["nombre"]}')
                return app
        print('Aplicacion no encontrada.')
        return None

    def descargar_app(self, nombre_app):
        app = self.buscar_app(nombre_app)
        if app:
            print(f'Aplicacion {nombre_app} descargada exitosamente.')
        else:
            print(f'No se pudo descargar la aplicacion {nombre_app} porque no fue encontrada.')

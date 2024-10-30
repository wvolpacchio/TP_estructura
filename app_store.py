from app import App
class AppStore:
    def __init__(self):
        self.aplicaciones_disponibles = [
            {"nombre": "WhatsApp", "version": "2.21", "categoria": "Social"},
            {"nombre": "Gmail", "version": "1.23", "categoria": "Productividad"},
            {"nombre": "Instagram", "version": "3.5", "categoria": "Social"}
        ]

    def buscar_app(self, nombre_app):
        for app in self.aplicaciones_disponibles:
            if app["nombre"].lower() == nombre_app.lower():
                print(f"Aplicacion encontrada: {app['nombre']} - Version: {app['version']}")
                return app
        print("Aplicacion no encontrada.")
        return None

    def descargar_app(self, telefono, nombre_app):
        app_info = self.buscar_app(nombre_app)
        if app_info:
            app = App(app_info["nombre"], app_info["version"], app_info["categoria"])
            telefono.dic_aplicaciones[app.nombre] = app  # Guardar una instancia de App
            print(f"Aplicación {app.nombre} descargada exitosamente en {telefono.nombre}.")
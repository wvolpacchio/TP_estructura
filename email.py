from datetime import datetime

class NodoEmail:
    """Nodo de la lista enlazada que representa un email en la bandeja de entrada."""
    def __init__(self, email):
        self.email = email
        self.siguiente = None

class ListaEnlazadaEmail:
    """Lista enlazada para almacenar y gestionar los emails en la bandeja de entrada."""
    def __init__(self):
        self.cabeza = None

    def agregar_email(self, email):
        nuevo_nodo = NodoEmail(email)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_email(self, id_email):
        actual = self.cabeza
        anterior = None
        index = 0
        while actual and index != id_email:
            anterior = actual
            actual = actual.siguiente
            index += 1
        if actual:
            if anterior:
                anterior.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
            print(f'Email de {actual.email["destinatario"]} eliminado.')
        else:
            print('ID de email no valido.')

    def mostrar_no_leidos(self):
        actual = self.cabeza
        while actual:
            if not actual.email['leido']:
                print(f"Email de {actual.email['destinatario']} - Asunto: {actual.email['asunto']}")
            actual = actual.siguiente

    def mostrar_por_fecha(self):
        emails = []
        actual = self.cabeza
        while actual:
            emails.append(actual.email)
            actual = actual.siguiente
        emails.sort(key=lambda x: x['fecha'], reverse=True)
        for email in emails:
            print(f"Email de {email['destinatario']} - Asunto: {email['asunto']}")

class Email:
    def __init__(self):
        self.bandeja_entrada = ListaEnlazadaEmail()

    def enviar_email(self, destinatario, asunto, cuerpo):
        email = {
            'destinatario': destinatario,
            'asunto': asunto,
            'cuerpo': cuerpo,
            'leido': False,
            'fecha': datetime.now()
        }
        print(f'Email enviado a {destinatario} con asunto: {asunto}')
        self.bandeja_entrada.agregar_email(email)

    def ver_email_no_leido(self):
        print("Mostrando emails no leidos:")
        self.bandeja_entrada.mostrar_no_leidos()

    def ver_email_por_fecha(self):
        print("Mostrando emails ordenados por fecha (ultimos primero):")
        self.bandeja_entrada.mostrar_por_fecha()

    def eliminar_email(self, id_email):
        print(f"Eliminando email en posicion {id_email}...")
        self.bandeja_entrada.eliminar_email(id_email)
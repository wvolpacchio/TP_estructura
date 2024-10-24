class Email:
    def __init__(self):
        self.bandeja_entrada = []
        self.emails_enviados = []

    def enviar_email(self, destinatario, asunto, cuerpo):
        email = {
            'destinatario': destinatario,
            'asunto': asunto,
            'cuerpo': cuerpo,
            'leido': False
        }
        self.emails_enviados.append(email)
        print(f'Email enviado a {destinatario} con asunto: {asunto}')

    def ver_email_no_leido(self):
        no_leidos = [email for email in self.bandeja_entrada if not email['leido']]
        if no_leidos:
            for email in no_leidos:
                print(f'Email de {email["destinatario"]}: {email["asunto"]}')
        else:
            print('No hay emails no leidos.')

    def ver_email_por_fecha(self):
        # Asumiendo que la bandeja de entrada tiene un campo 'fecha' para organizar
        emails_ordenados = sorted(self.bandeja_entrada, key=lambda x: x.get('fecha', ''))
        for email in emails_ordenados:
            print(f'Email de {email["destinatario"]} con asunto: {email["asunto"]}')

    def eliminar_email(self, id_email):
        if 0 <= id_email < len(self.bandeja_entrada):
            eliminado = self.bandeja_entrada.pop(id_email)
            print(f'Email de {eliminado["destinatario"]} eliminado.')
        else:
            print('ID de email no valido.')

class Llamada:
    def __init__(self):
        self.en_llamada = False

    def realizar_llamada(self, numero_destino):
        if not self.en_llamada:
            self.en_llamada = True
            print(f'Realizando llamada al numero {numero_destino}...')
        else:
            print('Ya estas en una llamada.')

    def recibir_llamada(self, numero_origen):
        if not self.en_llamada:
            self.en_llamada = True
            print(f'Recibiendo llamada del numero {numero_origen}...')
        else:
            print('No puedes recibir otra llamada. Ya estas en una.')

    def terminar_llamada(self):
        if self.en_llamada:
            self.en_llamada = False
            print('La llamada ha terminado.')
        else:
            print('No estas en una llamada.')

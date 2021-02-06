class Personaje:
    def __init__(self):
        self.supervivencia = 0

    def obtenerEstado(self):
        return 'Supervivencia: ' + str(self.supervivencia)
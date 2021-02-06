class Escenario:
    def __init__(self, descripcion, opciones):
        self.descripcion = descripcion
        self.opciones = opciones
        self.cambioSupervivencia = 0

    def presentar(self, personaje):
        print('\n')
        print(personaje.obtenerEstado())
        print(self.descripcion)

        personaje.supervivencia += self.cambioSupervivencia

        if personaje.supervivencia <= 0:
            print("Has tomado una mala decisión y has muerto. Puedes intentarlo de nuevo.")
            personaje.supervivencia = 0
            return 'INICIO'

        for i in range(len(self.opciones)):
            print("[" + str(i) + "] " + self.opciones[i].descripcion)

        error = True

        while error:
            eleccion = input()

            if eleccion.isnumeric():
                eleccion = int(eleccion)

                if eleccion < len(self.opciones):
                    error = False

            if error:
                print("¡Escribe el número de alguna de las opciones!")

            if not error:
                return self.opciones[eleccion].siguienteFragmento
                
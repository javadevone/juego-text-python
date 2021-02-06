import io

from Opcion import Opcion
from Escenario import Escenario
from Personaje import Personaje

personaje = Personaje()
escenarioActual = None
final = False
escenarios = {}


with io.open('EscenariosPrincipales.txt', 'r', encoding='utf8') as archivo:

    archivo.seek(0)
    contenido = archivo.read()

    partes = contenido.split("#")

    for p in range(len(partes)):

        if len(partes[p]) > 0:

            escenario = partes[p].split("*")
            partesEscenario = escenario[0].split("|")

            opciones = []

            for e in range(len(escenario)):

                if e > 0:
                    partesOpcion = escenario[e].split("|")
                    o = Opcion(partesOpcion[1].rstrip(), partesOpcion[0])
                    opciones.append(o)

            e = Escenario(partesEscenario[1], opciones)
            #2 contiene KO
            if 2 < len(partesEscenario):
                e.cambioSupervivencia = int(partesEscenario[2])
            escenarios[partesEscenario[0]] = e

escenarioActual = escenarios['INICIO']

while not final:
    siguiente = escenarioActual.presentar(personaje)
    escenarioActual = escenarios[siguiente]
class Barco ():
    def __init__(self, nombre, posiciones):
        self.nombre = nombre
        self.posiciones = posiciones


class Tablero():
    def __init__(self, id_jugador, dimensiones, barcos, tablero):
        self.id_jugador = id_jugador
        self.dimensiones = dimensiones
        self.barcos = barcos
        self.tablero = tablero


import variables as vars   

def coloca_barco(tupla_pos_tam_orientacion):
    tupla_pos_tam_orientacion = input() # en el input tendremos algo de la forma ((2,3), 2, N)
    pos = tupla_pos_tam_orientacion[0]
    tam = tupla_pos_tam_orientacion[1]
    orientacion = tupla_pos_tam_orientacion [2]

    for pieza in barco:
        tablero[pieza] = "O"
    return tablero

tablero = coloca_barco(tablero, barco1)
print(tablero)


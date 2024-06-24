import clases as c
import numpy as np
import funciones as f

# CONSTANTES
p_cardinales =["n","s","e","o"]
tam = 10
tam_barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
barco_a_poner = []


barcos = {"barco1": [(0,0),(0,1),(0,2),(0,3)], 
          "barco2": [(1,0),(1,1),(1,2)], "barco3": [(1,5),(1,6),(1,7)], 
          "barco4": [(2,0),(2,1)], "barco5": [(2,5),(2,6)], "barco6": [(2,8),(2,9)], 
          "barco7": [(3,0)], "barco8": [(3,2)], "barco9": [(3,4)], "barco10": [(3,6)],}

# VARIABLES
dic_tableros = {"jugador": np.full((tam, tam), " ", dtype=object), # donde estén nuestros barcos
                "jugador_disp": np.full((tam, tam), " ", dtype=object), # donde vamos a disparar
                "maquina": np.full((tam, tam), " ", dtype=object), 
                "maquina_disp": np.full((tam, tam), " ", dtype=object),}

dic_vidas = {"jugador": 20,"maquina": 20}
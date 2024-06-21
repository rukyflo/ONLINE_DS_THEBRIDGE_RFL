import numpy as np
import funciones as f

mi_tablero = np.full((10,10)," ")
tablero_maquina = np.full((10,10),"")

barcos = {"barco1": [(0,0),(0,1),(0,2),(0,3)], 
          "barco2": [(1,0),(1,1),(1,2)], "barco3": [(1,5),(1,6),(1,7)], 
          "barco4": [(2,0),(2,1)], "barco5": [(2,5),(2,6)], "barco6": [(2,8),(2,9)], 
          "barco7": [(3,0)], "barco8": [(3,2)], "barco9": [(3,4)], "barco10": [(3,6)],}

vidas = 20

diparo = "X"
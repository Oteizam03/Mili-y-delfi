# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:15:41 2026

@author: Delfina
"""

def registrar_habitos():
    habitos=[]
    while True:
        actividad = input("Ingrese una actividad. Si no hay mas ingrese salir: ")
        if actividad == "salir":
            break
        habitos.append(actividad)
    return habitos

actividad_usuario = registrar_habitos()
print(actividad_usuario)

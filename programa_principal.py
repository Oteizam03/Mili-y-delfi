# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:15:41 2026

@author: Delfina
"""

#Mili y delfi trabajo grupal probando 
#este contendra las funciones del programa

def registrar_habitos():
    habitos = []
    while True:
        actividad = input("ingrese una actividad. Si no hay mas ingrese salir: ")
        if actividad == "salir":
            break
        habitos.append(actividad)
    return habitos

actividad_usuario = registrar_habitos()
print (actividad_usuario)

def analizar_habitos(habitos):
    cant_actividad = {}
    
    for habito in habitos:
        if habito in cant_actividad:
            cant_actividad[habito] += 1
        else:
            cant_actividad[habito] = 1
    return cant_actividad
 
    
variable = analizar_habitos(actividad_usuario)
print(variable)

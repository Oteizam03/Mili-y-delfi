# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:15:41 2026

@author: Delfina
"""

#Mili y delfi trabajo grupal probando 
#este contendra las funciones del programa


def registrar_habitos():
    '''
    Registra los datos ingresados por el uruario y los guarda en una lista

    Returns
    -------
    habitos : list
        Lista con los habitos ingresados por el usuario.
        
    '''
    
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
    '''
    Analiza los habitos dentro de la lista y cuenta cuantas veces se encuentra cada habito en la lista

    Parameters
    ----------
    habitos : list
        Lista con los habitos ingresados por el usuario.

    Returns
    -------
    cant_actividad : dicc
        Diccionrio con un conteo de cuantas veces aparece cada habito en la lista.
        
    '''

    cant_actividad = {}
    
    for habito in habitos:
        if habito in cant_actividad:
            cant_actividad[habito] += 1
        else:
            cant_actividad[habito] = 1
    return cant_actividad
 
    
variable = analizar_habitos(actividad_usuario)
print(variable)


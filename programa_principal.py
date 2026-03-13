# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:37:30 2026

@author: Delfina
"""

import funciones_habitos

lista = funciones_habitos.registrar_habitos()
resultado = funciones_habitos.analizar_habitos(lista)

print(f"Resumen de Actividades: {resultado}")

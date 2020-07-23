#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:44:26 2020

@author: henry
"""


import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(
    lista_numeros)

series_b = pd.Series(
    tupla_numeros)

series_c = pd.Series(
    np_numeros)

series_d = pd.Series(
    [True,
    False,
    12,
    12.12,
    "Adrian",
    None,
    (1),
    [2],
    {"nombre":"Adrian"}
    ])

print(series_d[3])

lista_ciudades  = [
    "Ambato",
    "Cuenca",
    "Loja",
    "Quito"]

serie_ciudad = pd.Series(
    lista_ciudades,
    index = [
        "A",
        "C",
        "L",
        "Q"])

print(serie_ciudad[3])
print(serie_ciudad["C"])

valores_ciudad = {
    "Ibarra":9500,
    "Guayaquil":10000,
    "Cuenca":7000,
    "Quito":8000,
    "Loja":3000
    }

serie_valor_ciudad = pd.Series(
    valores_ciudad)


ciudades_menor_5k = serie_valor_ciudad < 5000

print(type(serie_valor_ciudad)) # pandas.core.series.Series'
print(type(ciudades_menor_5k))  # pandas.core.series.Series'
print(ciudades_menor_5k)


s5 = serie_valor_ciudad[ciudades_menor_5k]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

print("Lima" in serie_valor_ciudad)

svc_cuadrado = np.square(serie_valor_ciudad)

ciudades_uno = pd.Series({
    "Montañita":300,
    "Guayaquil":10000,
    "Quito":2000
    })

ciudades_dos = pd.Series({
    "Loja":300,
    "Guayaquil":10000
    })

ciudades_uno["Loja"] = 0


print(ciudades_uno + ciudades_dos)

ciudades_add = ciudades_uno.add(ciudades_dos)
#sub()
#mul()
#div()

ciud_concat = pd.concat([
    ciudades_uno,
    ciudades_dos])

ciud_concat_verify = pd.concat([
    ciudades_uno,
    ciudades_dos],
    verify_integrity = False)

ciud_concat_verify = ciudades_uno.append(
    ciudades_dos,
    verify_integrity = False)

print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))

print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))

print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))


print(ciudades_uno.head(2))
print(ciudades_uno.tail(2))

print(ciudades_uno.sort_values(
       ascending = False).head(2))
print(ciudades_uno.sort_values().head(2))

#0 - 1000%
#1001 - 5000 10%
#5001 - 20000 15%

def calcular(valor_serie):
    if (valor_serie <= 1000):
        return valor_serie * 1.005
    
    if (valor_serie > 1000 and valor_serie <= 5000):
        return valor_serie * 1.1
    
    if (valor_serie > 5000):
        return valor_serie * 1.15

ciudad_calculada = ciudades_uno.map(calcular)
























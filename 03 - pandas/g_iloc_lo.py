#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:27 2020

@author: henry
"""

#g_iloc_lo.py

import pandas as pd

path_guardado = "/home/henry/Documents/7moSemestre/Python/py-aguilar-quezada-henry-gonzalo/03 - pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

# loc

# primero = df.loc[1035]
# segundo = df.loc[1035, 'artist']

filtrado_horizontal = df.loc[1035] # Serie
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index) # Indices columnas

serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index) # Indices son los Indices

# Filtrado por indice
df_1035 = df[df.index == 1035]

# loc -> acceder grupo filas y columnas x LABEL (ARR TRUE FALSE)

segundo = df.loc[1035]  # Filtrar por indice (1)
segundo = df.loc[[1035,1036]] # Filtrar por arr indices

segundo = df.loc[3:5] # Filtrando desde x indice
                      # hasta y indice
segundo = df.loc[df.index == 1035] # Filtrar por 
                                   # Arreglo-> True False


segundo = df.loc[1035, 'artist'] # 1 Indice
segundo = df.loc[1035, ['artist', 'medium']] # Varios indices
segundo = df.loc[1035, ['artist', 'medium']]

# print(df.loc[0]) # Indice dentro del DataFrame X ERROR
# print(df[0]) # Indice dentro del DataFrame X ERROR

# iloc -> acceder grupo filas y columnas indices en 0

tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]


tercero = df.iloc[0:10, 0:4] # Filtrado indices
                             # Por rango de indice 0:4

#################

datos = {
    "nota 1":{
        "Pepito": 7,
        "Juanita": 8,
        "Maria": 9
        },
    "nota 2":{
        "Pepito": 7,
        "Juanita": 8,
        "Maria": 9
        },
    "disciplina":{
        "Pepito": 4,
        "Juanita": 9,
        "Maria": 2
        },
    }

notas = pd.DataFrame(datos)

condicion_nota = notas["nota 1"] <= 7
condicion_nota_dos = notas["nota 2"] <= 7
condicion_disc = notas["disciplina"] <= 7

mayores_siete = notas.loc[ condicion_nota, ["nota 1"]]

pasaron = notas.loc[condicion_nota][condicion_nota_dos][condicion_disc]

notas.loc["Maria", "disciplina"] = 7

notas.loc[:, "disciplina"] = 7

############ Promedio de las 3 notas (no1 + no2 + disc) / 3


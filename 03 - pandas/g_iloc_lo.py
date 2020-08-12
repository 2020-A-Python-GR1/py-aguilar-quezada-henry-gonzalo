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

#loc

filtrado_horizontal = df.loc[1035]
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index) #Indices columans

serie_vertical = df['artist']

print(serie_vertical)
print(serie_vertical.index) #Indices son los Indices

segundo = df.loc[1035]
segundo = df.loc[[1035,1036]]

segundo = df.loc[3:5]

segundo = df.loc[1035, 'artist']
segundo = df.loc[1035, ['artist', 'medium']]

#print(df.loc[0])

tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]

tercero = df.iloc[0:10, 0:4]


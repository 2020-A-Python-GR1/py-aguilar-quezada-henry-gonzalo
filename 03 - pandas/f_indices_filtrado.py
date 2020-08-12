#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:33:16 2020

@author: henry
"""

#f_indices_filtrado.py

import pandas as pd

path_guardado = "/home/henry/Documents/7moSemestre/Python/py-aguilar-quezada-henry-gonzalo/03 - pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(type(artistas))

print(artistas.size)

blake = df['artist'] == 'Blake, William'

print(blake.value_counts())

df_blake = df[blake]
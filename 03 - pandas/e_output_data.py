#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:55:14 2020

@author: henry
"""
# e_output_data.py

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = "/home/dev-11/Documents/Github/py-eguez-sarzosa-vicente-adrian/03 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

# Tipos Archivos

# JSON
# Excel
# SQL

# Excel #

path_excel = "/home/dev-11/Documents/Github/py-eguez-sarzosa-vicente-adrian/03 - Pandas/data/artwork_data.xlsx"
path_excel_indice = "/home/dev-11/Documents/Github/py-eguez-sarzosa-vicente-adrian/03 - Pandas/data/artwork_data_indice.xlsx"
path_excel_columnas = "/home/dev-11/Documents/Github/py-eguez-sarzosa-vicente-adrian/03 - Pandas/data/artwork_data_columnas.xlsx"

# artwork_data.xlsx
# artwork_data_indice.xlsx
# artwork_data_columnas.xlsx

# Con el indice como columna
# sub_df.to_excel(path_excel)

# Sin el indice como columna
# sub_df.to_excel(path_excel_indice, index = False)

columnas = ['artist', 'title', 'year']

sub_df.to_excel(path_excel_columnas, columns = columnas)

# Multiples hojas de trabajo #

path_excel_mt = "/home/henry/Documents/7moSemestre/Python/py-aguilar-quezada-henry-gonzalo/03 - Pandas/data/artwork_data_mt.xlsx"
# artwork_data_mt.xlsx

writer = pd.ExcelWriter(path_excel_mt, 
                        engine = 'xlsxwriter')

sub_df.to_excel(writer, sheet_name = 'Primera')

sub_df.to_excel(writer, sheet_name = 'Segunda')

sub_df.to_excel(writer, sheet_name = 'Tercera')

writer.save()

# Formato condicional #

path_excel_colores = "/home/henry/Documents/7moSemestre/Python/py-aguilar-quezada-henry-gonzalo/03 - Pandas/data/artwork_data_colores.xlsx"

# artwork_data_colores.xlsx

writer = pd.ExcelWriter(path_excel_colores, engine='xlsxwriter')
# Series

num_artistas = sub_df['artist'].value_counts()

print(type(num_artistas))
print(num_artistas)

num_artistas.to_excel(writer, sheet_name = 'Artistas')

# Seleccionando la hoja de trabajo #

hoja_artistas = writer.sheets['Artistas']

# Formato #

ultimo_numero = len(num_artistas.index) + 1

# rango_celdas = 'B2:B{}'.format()

rango_celdas = f'B2:B{ultimo_numero}' # B2:B85
rango_celdas_c = f'C2:C{ultimo_numero}' # C2:C85

print(rango_celdas)

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas, formato_artistas)
hoja_artistas.conditional_format(rango_celdas_c, formato_artistas)

writer.save()

########## SQL ##########

with sqlite3.connect("bdd_artist.bdd") as conexion:
    sub_df.to_sql('py_artistas', conexion)
    

## with mysql.connect('mysql://user:password@ip:puerto/nombre_base')
##      df5.to_sql('tabla_mysql', conexion)
    
########## JSON ##########

sub_df.to_json('artistas.json')

sub_df.to_json('artistas_tabla.json', orient = 'table')
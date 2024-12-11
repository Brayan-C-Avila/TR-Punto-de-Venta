import sys
import os

# Obtener la ruta absoluta del directorio actual (notebook)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar la ruta de la carpeta utils a sys.path
utils_path = os.path.join(current_dir, '..', 'utils') # Sube un nivel y entra a utils
sys.path.append(utils_path)

import tkinter as tk
from tkinter import ttk
from utils_consultas import filtrar_productos

def crear_pestaña_consulta(notebook, productos):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Consultar Productos")

    # Configuración para que las filas y columnas se expandan
    frame.grid_rowconfigure(1, weight=1)  # La fila con la tabla debe expandirse
    frame.grid_columnconfigure(0, weight=1)  # La columna debe expandirse

    # Frame para la barra de búsqueda y etiqueta
    search_frame = ttk.Frame(frame)
    search_frame.grid(row=0, column=0, sticky="w", padx=10, pady=5)

    search_label = ttk.Label(search_frame, text="Buscar Producto:")
    search_label.grid(row=0, column=0, padx=5)

    search_entry = ttk.Entry(search_frame, width=50)
    search_entry.grid(row=0, column=1, padx=5)

    # Tabla para mostrar productos
    columnas = ["ID", "Nombre", "Precio"]  # Definimos las columnas explícitamente
    productos_tree = ttk.Treeview(frame, columns=columnas, show="headings", height=20)
    
    # Establecer las cabeceras de la tabla
    for col in columnas:
        productos_tree.heading(col, text=col)
        productos_tree.column(col, width=150, anchor="w")
    
    # Hacer que la tabla tenga un borde y un fondo alternado
    productos_tree.tag_configure('even', background='#f2f2f2')  # Fondo alternado para filas
    productos_tree.tag_configure('odd', background='#ffffff')  # Fondo alternado para filas

    # Ajustar el tamaño de la fila para que sea más legible
    productos_tree.configure(height=20)

    # Empaquetar la tabla en la cuadrícula para que ocupe toda la columna
    productos_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Llamar a la función de filtrado cada vez que el texto en la barra de búsqueda cambie
    search_entry.bind("<KeyRelease>", lambda event: filtrar_productos(search_entry, productos_tree, productos))  # Re-filtrar al escribir

    # Inicialmente cargar todos los productos
    filtrar_productos(search_entry, productos_tree, productos)

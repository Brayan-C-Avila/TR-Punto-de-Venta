import tkinter as tk
import csv
from utils.utils_main import cargar_productos
from tkinter import ttk
from notebooks.notebook_consultas import crear_pestaña_consulta
from notebooks.notebook_ventas import crear_pestaña_ventas

# Archivo CSV con los productos
#archivo_csv = './productos_masivos_lite.csv'
archivo_csv = '../productos.csv'
productos = cargar_productos(archivo_csv)

# Ventana principal
root = tk.Tk()
icono = "./data/logo.ico"  
root.iconbitmap(icono)
root.title("TECNORED - Punto de Venta")
root.geometry("800x600")

# Crear el Notebook (Pestañas)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

style = ttk.Style()
style.configure('even.Treeview', background='white')
style.configure('odd.Treeview', background='lightgray')

# Crear pestañas
crear_pestaña_ventas(notebook, productos)
crear_pestaña_consulta(notebook, productos)

# Ejecutar aplicación
root.mainloop()

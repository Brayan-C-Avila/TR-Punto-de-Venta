#-- UTILS DEL MAIN.PY --#

import csv

def cargar_productos(archivo):
    """Lee el csv y retorna un diccionario con la informacion:
    Retorna:
        dict: Diccionario con productos donde la clave es el ID y el valor 
        es un diccionario con 'nombre' y 'precio'.
              Ejemplo: {'1': {'nombre': 'Manzana', 'precio': 5.5}, ...}
    """
    productos = {}
    with open(archivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convertir el ID a minúsculas antes de agregarlo al diccionario
            id_producto = row['id'].lower()  # Convertir el ID a minúsculas
            productos[id_producto] = {'nombre': row['nombre'], 'precio': float(row['precio'])}

    #print(productos)  # Esto te ayudará a verificar si los IDs están en minúsculas
    return productos

import pandas as pd
from faker import Faker
import csv
import random
import string

# Crear instancia de Faker con locale en español
fake = Faker('es_ES')  

num_productos = 30_000  # Ajusta la cantidad según lo necesario

def generar_id_alfanumerico(longitud=7):
    """Genera un ID alfanumérico de longitud específica."""
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def generar_productos(n):
    """Genera una lista de diccionarios con datos ficticios para productos."""
    productos = []
    for _ in range(n):
        productos.append({
            'id': generar_id_alfanumerico(),
            'nombre': fake.word().capitalize(),  # Generar un nombre sencillo
            'precio': round(random.uniform(1.00, 1000.00), 2),  # Precio aleatorio
            'categoria': fake.word().capitalize(),  # Categoría ficticia
            'descripcion': fake.sentence(nb_words=12),  # Descripción corta
        })
    return productos

# Escribe los datos al CSV en bloques para manejar grandes volúmenes de datos
bloque = 100000  # Ajusta el tamaño del bloque para optimizar el uso de memoria
with open('productos_masivos_lite.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'nombre', 'precio', 'categoria', 'descripcion'])  # Escribir encabezado

    for i in range(0, num_productos, bloque):
        # Generar productos en bloques
        productos = generar_productos(min(bloque, num_productos - i))
        # Convertir a DataFrame para escribir directamente al archivo CSV
        df = pd.DataFrame(productos)
        df.to_csv(csvfile, header=False, index=False)

print(f"Se generaron {num_productos} productos en 'productos_masivos.csv'")

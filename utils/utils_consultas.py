#-- UTILS DEL CONSULTAS.PY --#

from tkinter import ttk
import unidecode 

# Ejemplo de cómo configurar los estilos (hazlo una sola vez, al inicio de tu programa):


def filtrar_productos(search_entry, productos_tree, productos, mostrar_todos=True):
    """Filtra y muestra los productos en el Treeview según el término de búsqueda."""

    query = unidecode.unidecode(search_entry.get().strip().lower())
    query_keywords = query.split()

    # Limpiar el Treeview
    productos_tree.delete(*productos_tree.get_children())

    if not query_keywords and mostrar_todos:
        for index, (id_producto, producto) in enumerate(productos.items()):
            productos_tree.insert("", "end", values=(id_producto.upper(), producto['nombre'], f"${producto['precio']:.2f}"))  # Insertar sin etiquetas
        # Aplicar etiquetas al final
        for index, item in enumerate(productos_tree.get_children()):
            tag = 'even' if index % 2 == 0 else 'odd'
            productos_tree.item(item, tags=(tag,))
        return

    for index, (id_producto, producto) in enumerate(productos.items()):
        producto_values = [
            unidecode.unidecode(str(value).lower()) for value in [id_producto.upper(), producto['nombre'], producto['precio']]
        ]
        precio_str = f"{producto['precio']:.3f}"
        precio_str_normalizado = precio_str.replace(".", "")

        if any(keyword in value for keyword in query_keywords for value in producto_values):
            resaltado = [
                value.replace(query, f"[{query}]") if query in value else value
                for value in producto_values
            ]

            if any(keyword.replace(".", "") == precio_str_normalizado for keyword in query_keywords):
                continue

            # Insertar sin etiquetas
            productos_tree.insert("", "end", values=(resaltado[0], resaltado[1], f"${producto['precio']:.2f}"))

    # Aplicar etiquetas 'even' y 'odd' después de insertar todas las filas
    for index, item in enumerate(productos_tree.get_children()):
        tag = 'even' if index % 2 == 0 else 'odd'
        productos_tree.item(item, tags=(tag,))


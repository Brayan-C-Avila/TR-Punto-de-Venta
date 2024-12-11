import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.utils_ventas import eliminar_producto, actualizar_carrito, agregar_producto, cancelar_compra, finalizar_compra

def solo_numeros(entry_value):
    """Función para permitir solo números y un punto decimal."""
    if entry_value == "" or entry_value.isdigit() or (entry_value.count('.') == 1 and entry_value.replace('.', '').isdigit()):
        return True
    else:
        return False

def crear_pestaña_ventas(notebook, productos):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="  Realizar Ventas  ")

    carrito = {}

    # Sección del total en la parte superior
    total_label = tk.Label(frame, text="TOTAL: $0.00", font=("Arial", 18), fg="black")
    total_label.pack(pady=10)

    # Frame para la selección de productos
    seleccionar_frame = ttk.Frame(frame)
    seleccionar_frame.pack(fill="x", padx=10, pady=10)

    ttk.Label(seleccionar_frame, text="ID del Producto:").pack(side="left", padx=5)
    
    # No validamos para el ID del Producto, se deja como texto normal
    id_var = tk.StringVar()
    ttk.Entry(seleccionar_frame, textvariable=id_var, width=10).pack(side="left", padx=5)

    ttk.Label(seleccionar_frame, text="Cantidad:").pack(side="left", padx=5)
    cantidad_var = tk.IntVar(value=1)
    ttk.Entry(seleccionar_frame, textvariable=cantidad_var, width=10).pack(side="left", padx=5)

    ttk.Button(seleccionar_frame, text="Agregar al Carrito", command=lambda: agregar_producto(id_var.get(), cantidad_var.get(), productos, carrito, carrito_tree, total_label)).pack(side="left", padx=5)
    ttk.Button(seleccionar_frame, text="Cancelar Compra", command=lambda: cancelar_compra(carrito, carrito_tree, total_label)).pack(side="left", padx=5)

    # Tabla del carrito
    carrito_tree = ttk.Treeview(frame, columns=("ID", "Producto", "Cantidad", "Subtotal"), show="headings", height=15)
    carrito_tree.heading("ID", text="ID")
    carrito_tree.heading("Producto", text="Producto")
    carrito_tree.heading("Cantidad", text="Cantidad")
    carrito_tree.heading("Subtotal", text="Subtotal")
    carrito_tree.column("ID", width=30)
    carrito_tree.column("Producto", width=200)
    carrito_tree.column("Cantidad", width=100)
    carrito_tree.column("Subtotal", width=100)

    # Configurar los colores alternos para las filas
    carrito_tree.tag_configure('even', background='#f2f2f2')  # Fondo alternado para filas
    carrito_tree.tag_configure('odd', background='#ffffff')  # Fondo alternado para filas

    carrito_tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Crear el menú emergente (pop-up menu)
    menu = tk.Menu(frame, tearoff=0)
    menu.add_command(label="Eliminar Producto", command=lambda: eliminar_producto(carrito, carrito_tree, total_label, productos))

    # Función para mostrar el menú contextual al hacer clic derecho
    def mostrar_menu(event):
        menu.post(event.x_root, event.y_root)

    # Asociar el evento de clic derecho con el Treeview
    carrito_tree.bind("<Button-3>", mostrar_menu)  # El evento <Button-3> es clic derecho

    # Función para detectar la tecla Supr y eliminar el producto
    def detectar_supr(event):
        eliminar_producto(carrito, carrito_tree, total_label, productos)

    # Asociar la tecla Supr con la función de eliminar producto
    carrito_tree.bind("<Delete>", detectar_supr)  # <Delete> es la tecla Supr en el teclado

    # Frame para el pago
    finalizar_frame = ttk.Frame(frame)
    finalizar_frame.pack(fill="x", padx=10, pady=10)

    ttk.Label(finalizar_frame, text="Pago:").pack(side="left", padx=5)
    
    # Validación solo para números y un punto decimal (para el pago)
    vcmd_pago = (frame.register(solo_numeros), "%P")  # %P es el valor actual del Entry
    pago_var = tk.StringVar()
    pago_label = ttk.Entry(finalizar_frame, textvariable=pago_var, width=10, validate="key", validatecommand=vcmd_pago)
    pago_label.pack(side="left", padx=5)

    ttk.Button(finalizar_frame, text="Finalizar Compra", command=lambda: finalizar_compra(carrito, productos, pago_var, carrito_tree, total_label, pago_label)).pack(side="left", padx=5)

#-- UTILS VENTAS.PY --#

import tkinter as tk
from tkinter import messagebox, ttk
from decimal import Decimal, getcontext

# Establecer el contexto global de los decimales (con precisión de 2 decimales)
getcontext().prec = 6  # Puedes ajustar la precisión según sea necesario


# Función para actualizar el carrito
def actualizar_carrito(carrito_tree, carrito, productos, total_label):
    carrito_tree.delete(*carrito_tree.get_children())
    total = Decimal('0.00')
    for index, (id_producto, cantidad) in enumerate(carrito.items()):
        producto = productos[id_producto]
        subtotal = Decimal(producto['precio']) * cantidad
        total += subtotal
        tag = 'even' if index % 2 == 0 else 'odd'  # Asignar tag para fondo alternado
        carrito_tree.insert("", "end", values=(producto['nombre'], cantidad, f"${subtotal:.2f}"), tags=(tag,))
    total_label.config(text=f"TOTAL: ${total:.2f}")


# Función para agregar producto al carrito
def agregar_producto(id_producto, cantidad, productos, carrito, carrito_tree, total_label):
    #print(f"ID: {productos}")
    # Normalizar id para evitar fallos al buscar
    id_producto = id_producto.lower().replace(" ", "")

    if id_producto in productos:
        if cantidad > 0:
            # Guardar tanto la cantidad como el precio unitario en el carrito
            if id_producto in carrito:
                carrito[id_producto]['cantidad'] += cantidad
            else:
                carrito[id_producto] = {
                    'cantidad': cantidad,
                    'precio': productos[id_producto]['precio']
                }
            actualizar_carrito(carrito_tree, carrito, productos, total_label)
        else:
            messagebox.showerror("Error", "La cantidad debe ser mayor a cero.")
    else:
        messagebox.showerror("Error", "Producto no encontrado.")


# Función para cancelar la compra
def cancelar_compra(carrito, carrito_tree, total_label, productos):
    #print(carrito)
    carrito.clear()
    #print(carrito)
    actualizar_carrito(carrito_tree, carrito, productos, total_label)


def finalizar_compra(carrito, productos, pago_var, carrito_tree, total_label, pago_label):
    """Función para finalizar la compra."""
    try:
        total = sum(Decimal(productos[id_producto]['precio']) * datos['cantidad'] for id_producto, datos in carrito.items())
        pago = Decimal(pago_var.get())

        if pago >= total:
            cambio = pago - total
            messagebox.showinfo("Compra finalizada", f"Total: ${total:.2f}\t\n\nPago: ${pago:.2f}\t\t\n\nCambio: ${cambio:.2f}", icon="info")
            carrito.clear()  # Vacía el carrito
            actualizar_carrito(carrito_tree, carrito, productos, total_label)

            pago_var.set("")
            if hasattr(pago_label, 'delete'):  # Verifica si pago_label tiene el método delete
                pago_label.delete(0, 'end')  # Borra el contenido si es un Entry
            elif hasattr(pago_label, 'config'):
                 pago_label.config(text="") # Borra el contenido si es un Label
        else:
            messagebox.showerror("Error", "El pago es insuficiente.")

    except (ValueError, KeyError) as e:  # Captura errores de conversión y claves no encontradas
        messagebox.showerror("Error", f"Ha ocurrido un error:\n{str(e)}")

def actualizar_carrito(carrito_tree, carrito, productos, total_label):
    # Limpiar la tabla
    carrito_tree.delete(*carrito_tree.get_children())

    # Variables para el cálculo total
    total = 0

    # Llenar el Treeview
    for index, (producto_id, datos) in enumerate(carrito.items()):
        cantidad = datos['cantidad']
        precio_unitario = datos['precio']
        subtotal = cantidad * precio_unitario
        total += subtotal

        # Alternar colores
        tag = 'even' if index % 2 == 0 else 'odd'

        # Insertar fila en el Treeview
        carrito_tree.insert("", "end", values=(
            producto_id.upper(),
            productos[producto_id]['nombre'],
            cantidad,
            f"${precio_unitario:.2f}",
            f"${subtotal:.2f}"
        ), tags=(tag,))

    # Actualizar el total
    total_label.config(text=f"TOTAL: ${total:.2f}")





def eliminar_producto(carrito, carrito_tree, total_label, productos):
    """Función para eliminar un producto del carrito."""
    # Obtener el ID del producto seleccionado
    print(f"carrito tree: {carrito_tree}\n\n\n")
    print(f"carrito: {carrito}\n\n\n")

    selected_item = carrito_tree.selection()
    print(f"SELECTE_ITEN: {selected_item}")
    if True:
        #print("DENTRO DE IF")
        producto_id = str(carrito_tree.item(selected_item, 'values')[0])  # Obtener el ID del producto
        producto_id = producto_id.lower()
        #print(f"Producto seleccionado para eliminar: {producto_id}")  # Ver para depuración
        #print(f"carrito: {carrito}")
        if producto_id in carrito:
            del carrito[producto_id]  # Eliminar del carrito
            #print(f"CARRITO ELIMINADO: {carrito}")
            actualizar_carrito(carrito_tree, carrito, productos, total_label)  # Actualizar la tabla
        else:
            messagebox.showerror("Error", "Producto no encontrado en el carrito.")
    else:
        messagebox.showerror("Error", "Debe seleccionar un producto para eliminar.")

def modificar_cantidad(carrito, carrito_tree, total_label, productos):
    """Función para modificar la cantidad de un producto en el carrito."""
    selected_item = carrito_tree.selection()

    if not selected_item:
        messagebox.showerror("Error", "Debe seleccionar un producto para modificar.")
        return

    # Obtener el ID del producto seleccionado
    producto_id = str(carrito_tree.item(selected_item, 'values')[0]).lower()

    if producto_id not in carrito:
        messagebox.showerror("Error", "Producto no encontrado en el carrito.")
        return

    # Función para validar que solo se ingresen números.
    def solo_numeros(entry_value):
        return entry_value.isdigit() or entry_value == ""

    # Crear una nueva ventana emergente
    popup = tk.Toplevel()
    popup.title("Modificar Cantidad")
    popup.geometry("300x150")
    popup.resizable(False, False)

    ttk.Label(popup, text=f"Modificar cantidad para: {productos[producto_id]['nombre']}").pack(pady=10)

    cantidad_var = tk.StringVar()
    cantidad_entry = ttk.Entry(popup, textvariable=cantidad_var, validate="key",
                               validatecommand=(popup.register(solo_numeros), "%P"))
    cantidad_entry.pack(pady=10)

    cantidad_entry.focus()  # Enfocar automáticamente en el campo de entrada

    def guardar_cantidad():
        nueva_cantidad = cantidad_var.get()

        if not nueva_cantidad or int(nueva_cantidad) <= 0:
            messagebox.showerror("Error", "Ingrese una cantidad válida.", parent=popup)
            return

        # Actualizar SOLO la cantidad en el carrito
        carrito[producto_id]['cantidad'] = int(nueva_cantidad)  # Corrección aquí
        actualizar_carrito(carrito_tree, carrito, productos, total_label)

        popup.destroy()

    # Frame para los botones
    button_frame = ttk.Frame(popup)
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="Cancelar", command=popup.destroy).pack(side="left", padx=5)
    ttk.Button(button_frame, text="Guardar", command=guardar_cantidad).pack(side="left", padx=5)

    popup.mainloop()


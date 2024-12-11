# Punto de Venta Personalizado para TECNORED

Este proyecto es una solución de punto de venta (POS) personalizada para **TECNORED**, desarrollada en Python utilizando la librería **Tkinter**. La aplicación está diseñada para gestionar productos y ventas, utilizando un archivo `.csv` para almacenar la información de los productos. Además, permite la interacción con una interfaz gráfica que sigue un modelo tipo "notebook" para facilitar la navegación entre las distintas secciones.

## Características

- **Interfaz gráfica de usuario (GUI):** Desarrollada con Python y Tkinter, permite una experiencia amigable y accesible.
- **Productos desde archivo CSV:** Los productos se cargan desde un archivo CSV, lo que facilita la actualización de inventario.
- **Múltiples secciones:** Utiliza una interfaz tipo notebook, donde cada sección se organiza en pestañas para un acceso rápido.
- **Carpetas de recursos:**
  - **notebooks**: Contiene las diferentes secciones graficas del sistema como `notebook_ventas.py`.
  - **utils**: Contiene las funciones que se realizan al interactuar con la interfaz como `utils_ventas.py` .
  - **datos**: Contiene los archivos de datos como el CSV de productos, los logos, iconos y archivos de sonido (ej. `beep.mp3`).

## Instalación

Para usar el proyecto en tu máquina local, sigue estos pasos:

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/Brayan-C-Avila/TR-Punto-de-venta.git
    ```

2. **Instalar las dependencias necesarias:**

    Este proyecto utiliza **Tkinter**, que es parte de la librería estándar de Python. Solo necesitas instalar Python en tu sistema:

    - Descarga Python desde [aquí](https://www.python.org/downloads/).
    - Asegúrate de tener la versión 3.11.x instalada.

3. **Ejecutar la aplicación:**

    Una vez que hayas clonado el repositorio y hayas instalado las dependencias, puedes ejecutar la aplicación con el siguiente comando:

    ```bash
    python main.py
    ```

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
/Punto-de-Venta
│
├── main.py                 # Archivo principal que ejecuta la aplicación
├── /notebooks              # Carpeta con las secciones graficas del sistema 
│   ├── notebook_ventas.py
│   └── ...
├── /utils                  # Funciones auxiliares
│   ├── notebook_ventas.py  
│   └── ...
├── /datos                  # Archivos de datos y recursos
│   └── ...
└── /__pycache__            # Archivos compilados de Python
```

## Funcionalidades

1. **Interfaz de usuario tipo Notebook:**
   - Se crea una ventana principal usando Tkinter con un estilo "notebook" (pestañas), donde cada pestaña puede tener una funcionalidad diferente.
   
2. **Gestión de productos:**
   - Los productos son cargados desde un archivo CSV y se pueden agregar, editar y eliminar productos.

3. **Extensibilidad:**
   - Este es solo un prototipo de la primera versión. Se planean nuevas características y mejoras, como la gestión de ventas, usuarios y más funcionalidades de administración.

## Contribución

Este proyecto está en su **primera versión**, por lo que las contribuciones son bienvenidas. Si tienes ideas para mejorar la aplicación o encontrar algún error, no dudes en abrir un **issue** o enviar un **pull request**.

## To-Do

- [ ] Añadir más funcionalidades en el área de ventas.
- [ ] Mejorar la interfaz gráfica para hacerla más intuitiva.
- [ ] Implementar almacenamiento de ventas en otro formato (base de datos, por ejemplo).
- [ ] Agregar más sonidos y recursos visuales.
- [ ] Realizar pruebas de usabilidad y rendimiento.

## Licencia

Este proyecto está bajo la licencia MIT.

---

import tkinter as tk
from tkinter import ttk
from cosas import distribuciones


# ventana que se mostrara dentro del frame de la pantalla de inicio
def uniformeV(ventana):
    # Crear un frame para la "ventana interna"
    internal_frame = tk.Frame(ventana,  relief=tk.RIDGE, bg="white")

    # Ubicar el frame en el centro de la pantalla
    internal_frame.grid(row=1, column=0)

    # etiqueta de texto
    label1 = tk.Label(internal_frame, text="Cantidad de numeros a generar")
    label1.pack()

    # para cargar numero
    numero1 = tk.Entry(internal_frame)
    numero1.pack()

    # etiqueta de texto
    label2 = tk.Label(internal_frame, text="Ingresar valor de limite inferior:")
    label2.pack()

    # para cargar numero
    numero2 = tk.Entry(internal_frame)
    numero2.pack()

    # etiqueta de texto
    label3 = tk.Label(internal_frame, text="Ingresar valor de limite superior:")
    label3.pack()

    # para cargar numero
    numero3 = tk.Entry(internal_frame)
    numero3.pack()

    # lbl donde guardaras res
    res = tk.Label(internal_frame, text="res:")
    res.pack()

    # es un boton        v            texto a mostrar                   para invocar una fun que necesita parametros
    boton = tk.Button(internal_frame, text="Calcular", command=lambda: distribuciones.uniforme(int(numero1.get()), int(numero2.get()), int(numero3.get()), table))
    boton.pack()

    table = ttk.Treeview(internal_frame, columns=("Numeros"))
    table.pack()

    # Agregar un botón en la "ventana interna"
    button = tk.Button(internal_frame, text="Cerrar ventana", command=internal_frame.destroy)
    button.pack(pady=10)
    return table


# ventana que se mostrara dentro del frame de la pantalla de inicio
def exponencialV(ventana):
    # Crear un frame para la "ventana interna"
    internal_frame = tk.Frame(ventana, width=1980, height=720, bg="white")

    # Ubicar el frame en el centro de la pantalla
    internal_frame.grid(row=1, column=0)

    # etiqueta de texto
    label1 = tk.Label(internal_frame, text="Cantidad de numeros a generar")
    label1.pack()

    # para cargar numero
    numero1 = tk.Entry(internal_frame)
    numero1.pack()

    # etiqueta de texto
    label2 = tk.Label(internal_frame, text="Ingresar Media:")
    label2.pack()

    # para cargar numero
    numero2 = tk.Entry(internal_frame)
    numero2.pack()

    # lbl donde guardaras res
    res = tk.Label(internal_frame, text="res:")
    res.pack()

    # es un boton        v            texto a mostrar                   fun que necesita parametros
    boton = tk.Button(internal_frame, text="Calcular", command=lambda: distribuciones.exponencial(int(numero1.get()), int(numero2.get()), table))
    boton.pack()

    table = ttk.Treeview(internal_frame, columns=("Numeros"))
    table.pack()

    # Agregar un botón en la "ventana interna"
    button = tk.Button(internal_frame, text="Cerrar ventana", command=internal_frame.destroy)
    button.pack(pady=10)


def poissonV(ventana):
    # Crear un frame para la "ventana interna"
    internal_frame = tk.Frame(ventana,  bg="white")

    # Ubicar el frame en el centro de la pantalla
    internal_frame.grid(row=1, column=0)

    # etiqueta de texto
    label1 = tk.Label(internal_frame, text="Cantidad de numeros a generar")
    label1.pack()

    # para cargar numero
    numero1 = tk.Entry(internal_frame)
    numero1.pack()

    # etiqueta de texto
    label2 = tk.Label(internal_frame, text="Ingresar Media:")
    label2.pack()

    # para cargar numero
    numero2 = tk.Entry(internal_frame)
    numero2.pack()

    # lbl donde guardaras res
    res = tk.Label(internal_frame, text="res:")
    res.pack()

    # es un boton        v            texto a mostrar                   fun que necesita parametros
    boton = tk.Button(internal_frame, text="Calcular", command=lambda: distribuciones.poisson(int(numero2.get()), int(numero1.get()), table))
    boton.pack()

    table = ttk.Treeview(internal_frame, columns=("Numeros"))
    table.pack()

    # Agregar un botón en la "ventana interna"
    button = tk.Button(internal_frame, text="Cerrar ventana", command=internal_frame.destroy)
    button.pack(pady=10)




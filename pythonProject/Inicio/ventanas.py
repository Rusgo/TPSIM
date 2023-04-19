import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Inicio
import distribuciones

is_open = False


# ventana que se mostrara dentro del frame de la pantalla de inicio
def uniformeV(ventana, tabla,tabla_numeros, resultadoBondad, tab):
    global is_open
    if not is_open:

        is_open = True
        # Crear un frame para la "ventana interna"
        internal_frame = tk.Frame(ventana, relief=tk.RIDGE, bg="white")

        # Ubicar el frame en el centro de la pantalla
        internal_frame.grid(row=2, column=0)

        titulo_u = tk.Label(internal_frame, text="Uniforme", font=("Arial", 16, "bold"))
        titulo_u.pack()

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

        # cantidad de intervalos adsasdasd
        res = tk.Label(internal_frame, text="Ingrese Cantidad de intervalos")
        res.pack()
        interv = tk.Entry(internal_frame)
        interv.pack()

        # es un boton        v            texto a mostrar                   para invocar una fun que necesita parametros
        boton = tk.Button(internal_frame, text="Calcular", command=lambda: distribuciones.uniforme(int(numero1.get()),
                                                                                                   int(numero2.get()),
                                                                                                   int(numero3.get()),
                                                                                                   int(interv.get()),
                                                                                                   tabla,tabla_numeros,resultadoBondad ))
        boton.pack()

        # Agregar un botón en la "ventana interna"
        button = tk.Button(internal_frame, text="Cerrar ventana", command=lambda: cerrar(internal_frame,tabla,tab))
        button.pack(pady=10)
    else:
        messagebox.showinfo("info", "Cierre el modelo actual para abrir otro")


# ventana que se mostrara dentro del frame de la pantalla de inicio
def exponencialV(ventana,tabla,tabla_numeros,resultadoBondad,tab):
    global is_open
    if not is_open:

        is_open = True
        # Crear un frame para la "ventana interna"
        internal_frame = tk.Frame(ventana, width=1980, height=720, bg="white")

        # Ubicar el frame en el centro de la pantalla
        internal_frame.grid(row=2, column=0)

        titulo_e = tk.Label(internal_frame, text="Exponencial", font=("Arial", 16, "bold"))
        titulo_e.pack()

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

        # cantidad de intervalos adsasdasd
        res = tk.Label(internal_frame, text="Ingrese Cantidad de intervalos")
        res.pack()
        interv = tk.Entry(internal_frame)
        interv.pack()
        # es un boton        v            texto a mostrar                   fun que necesita parametros
        boton = tk.Button(internal_frame, text="Calcular",
                          command=lambda: distribuciones.exponencial(int(numero1.get()),
                                                                     int(numero2.get()),
                                                                     int(interv.get()), tabla,tabla_numeros,resultadoBondad ))
        boton.pack()
        # Agregar un botón en la "ventana interna"
        button = tk.Button(internal_frame, text="Cerrar ventana", command=lambda: cerrar(internal_frame,tabla,tab))
        button.pack(pady=10)
    else:
        messagebox.showinfo("info", "Cierre el modelo actual para abrir otro")


def poissonV(ventana,tabla,tabla_numeros,resultadoBondad ):
    global is_open
    if not is_open:
        is_open = True
        # Crear un frame para la "ventana interna"
        internal_frame = tk.Frame(ventana, bg="white")

        # Ubicar el frame en el centro de la pantalla
        internal_frame.grid(row=2, column=0)

        titulo_p = tk.Label(internal_frame, text="Poisson", font=("Arial", 16, "bold"))
        titulo_p.pack()

        # etiqueta de texto
        label1 = tk.Label(internal_frame, text="Cantidad de numeros a generar")
        label1.pack()

        # para cargar numero
        numerosGenerar = tk.Entry(internal_frame)
        numerosGenerar.pack()

        # etiqueta de texto
        label2 = tk.Label(internal_frame, text="Ingresar Media:")
        label2.pack()

        # para cargar numero
        media = tk.Entry(internal_frame)
        media.pack()


        # es un boton        v            texto a mostrar                   fun que necesita parametros
        boton = tk.Button(internal_frame, text="Calcular", command=lambda: distribuciones.poisson(int(media.get()),
                                                                                                  int(numerosGenerar.get()),
                                                                                                  tabla,tabla_numeros ,resultadoBondad))
        boton.pack()

        # Agregar un botón en la "ventana interna"
        button = tk.Button(internal_frame, text="Cerrar ventana", command=lambda: cerrar(internal_frame,tabla,tab))
        button.pack(pady=10)
    else:
        messagebox.showinfo("info", "Cierre el modelo actual para abrir otro")


def normalV(ventana,tabla,tabla_numeros,resultadoBondad,tab ):
    global is_open
    if not is_open:
        is_open = True
        # Crear un frame para la "ventana interna"
        internal_frame = tk.Frame(ventana, bg="white")

        # Ubicar el frame en el centro de la pantalla
        internal_frame.grid(row=2, column=0)

        titulo_n = tk.Label(internal_frame, text="Normal", font=("Arial", 16, "bold"))
        titulo_n.pack()

        # etiqueta de texto
        label1 = tk.Label(internal_frame, text="Cantidad de numeros a generar")
        label1.pack()

        # para cargar numero
        numeros_a_generar = tk.Entry(internal_frame)
        numeros_a_generar.pack()

        # etiqueta de texto
        txt_media = tk.Label(internal_frame, text="Ingresar Media:")
        txt_media.pack()

        # para cargar numero
        media = tk.Entry(internal_frame)
        media.pack()

        # etiqueta de texto
        txt_de = tk.Label(internal_frame, text="Ingresar De:")
        txt_de.pack()

        # para cargar numero
        de = tk.Entry(internal_frame)
        de.pack()
        # cantidad de intervalos adsasdasd
        res = tk.Label(internal_frame, text="Ingrese Cantidad de intervalos")
        res.pack()
        interv = tk.Entry(internal_frame)
        interv.pack()

        # es un boton        v            texto a mostrar                   fun que necesita parametros
        boton = tk.Button(internal_frame, text="Calcular", command=lambda: distribuciones.normal(
            int(numeros_a_generar.get()),
            int(media.get()),
            int(de.get()),
            int(interv.get()), tabla,tabla_numeros,resultadoBondad ))
        boton.pack()

        table = ttk.Treeview(internal_frame, columns="Numeros")

        # Agregar un botón en la "ventana interna"
        button = tk.Button(internal_frame, text="Cerrar ventana", command=lambda: cerrar(internal_frame,tabla,tab))
        button.pack(pady=10)
    else:
        messagebox.showinfo("info", "Cierre el modelo actual para abrir otro")


def cerrar(i, tabla, tabla_n):
    tabla.delete(*tabla.get_children())
    tabla_n.delete(*tabla_n.get_children())
    colu = ["", "", "", "", "", "", "", "", ""]
    tabla.column(column="#0", width=100, minwidth=50, anchor='w')
    tabla.heading(column="#0", text="vacio", anchor='w')
    for col, nombre_columna in enumerate(colu):
        tabla.column(column=col, width=100, minwidth=50, anchor='w')
        tabla.heading(column=col, text=nombre_columna, anchor='w')
    i.destroy()
    global is_open
    is_open = False


def preparar_tabla_ks(tabla):
    tabla.column(column="#0", width=100, minwidth=50, anchor='w')
    tabla.heading(column="#0", text="Prueba KS", anchor='w')
    colu = ["d-h", "fo", "fe", "po", "pe", "poacu", "peacu", "dif", "max"]
    for col, nombre_columna in enumerate(colu):
        tabla.column(column=col, width=100, minwidth=50, anchor='w')
        tabla.heading(column=col, text=nombre_columna, anchor='w')


def preparar_tabla_chi(tabla):
    tabla.column(column="#0", width=100, minwidth=50, anchor='w')
    tabla.heading(column="#0", text="Prueba chi2", anchor='w')
    colu = ["d-h", "fo", "fe", "c", "c_acu", "", "", "", ""]
    for col, nombre_columna in enumerate(colu):
        tabla.column(column=col, width=100, minwidth=50, anchor='w')
        tabla.heading(column=col, text=nombre_columna, anchor='w')


def preparar_tabla_chi_poisson(tabla):
    tabla.column(column="#0", width=100, minwidth=50, anchor='w')
    tabla.heading(column="#0", text="Prueba chi2", anchor='w')
    colu = ["Numeros", "fo", "fe", "c", "c_acu", "", "", "", ""]
    for col, nombre_columna in enumerate(colu):
        tabla.column(column=col, width=100, minwidth=50, anchor='w')
        tabla.heading(column=col, text=nombre_columna, anchor='w')
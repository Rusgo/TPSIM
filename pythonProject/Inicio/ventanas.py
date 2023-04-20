import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import distribuciones
select = "media"
is_open = False
select2 = "1"


# ventana que se mostrara dentro del frame de la pantalla de inicio
def uniformeV(ventana, tabla,tabla_numeros, resultadoBondad, tab):
    global is_open
    if not is_open:

        is_open = True
        # Crear un frame para la "ventana interna"
        internal_frame = tk.Frame(ventana, bg="white", bd=2, relief=tk.RIDGE)
        # Ubicar el frame en el centro de la pantalla
        internal_frame.grid(row=2, column=1)

        titulo_u = tk.Label(internal_frame, text="Uniforme", font=("Arial", 16, "bold"))
        titulo_u.pack()

        # etiqueta de texto
        label1 = tk.Label(internal_frame, text="Cantidad de numeros a generar", bg="white")
        label1.pack()

        # para cargar numero
        numero1 = tk.Entry(internal_frame)
        numero1.pack()

        # etiqueta de texto
        label2 = tk.Label(internal_frame, text="Ingresar valor de limite inferior:", bg="white")
        label2.pack()

        # para cargar numero
        numero2 = tk.Entry(internal_frame)
        numero2.pack()

        # etiqueta de texto
        label3 = tk.Label(internal_frame, text="Ingresar valor de limite superior:", bg="white")
        label3.pack()

        # para cargar numero
        numero3 = tk.Entry(internal_frame)
        numero3.pack()

        # cantidad de intervalos adsasdasd
        res = tk.Label(internal_frame, text="Ingrese Cantidad de intervalos", bg="white")
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
def exponencialV(ventana, tabla, tabla_numeros, resultadoBondad,tab):
    global is_open
    if not is_open:
        is_open = True
        # Crear un frame para la "ventana interna"
        internal_frame = tk.Frame(ventana, bg="white", bd=2, relief=tk.RIDGE)
        # Ubicar el frame en el centro de la pantalla
        internal_frame.grid(row=2, column=1)

        titulo_e = tk.Label(internal_frame, text="Exponencial", font=("Arial", 16, "bold"))
        titulo_e.pack()

        # etiqueta de texto
        label1 = tk.Label(internal_frame, text="Cantidad de numeros a generar", bg="white")
        label1.pack()

        # para cargar numero
        numero1 = tk.Entry(internal_frame)
        numero1.pack()


        # Seleccionar una opción por defecto
        opcion_seleccionada = tk.StringVar(value="media")

        global select
        select = "media"

        def imprimir_opcion():
            global select
            select = str(opcion_seleccionada.get())

        # Función para cambiar la opción seleccionada
        def cambiar_opcion(opcion):
            opcion_seleccionada.set(opcion)

        # Crear los botones de selección
        opcion1 = tk.Radiobutton(internal_frame, text="media", variable=opcion_seleccionada, value="media",
                                 command=imprimir_opcion)
        opcion2 = tk.Radiobutton(internal_frame, text="lambda", variable=opcion_seleccionada, value="lambda",
                                 command=imprimir_opcion)
        # Empaquetar los botones en la ventana
        opcion1.pack()
        opcion2.pack()
        # etiqueta de texto
        label2 = tk.Label(internal_frame, text="Ingresar valor:", bg="white")
        label2.pack()

        # para cargar numero
        numero2 = tk.Entry(internal_frame)
        numero2.pack()

        # cantidad de intervalos adsasdasd
        res = tk.Label(internal_frame, text="Ingrese Cantidad de intervalos", bg="white")
        res.pack()
        interv = tk.Entry(internal_frame)
        interv.pack()
        # es un boton        v            texto a mostrar                   fun que necesita parametros
        boton = tk.Button(internal_frame, text="Calcular",
                          command=lambda: distribuciones.exponencial(int(numero1.get()),
                                                                     float(numero2.get()),
                                                                     int(interv.get()), tabla,tabla_numeros,resultadoBondad , select))
        boton.pack()
        # Agregar un botón en la "ventana interna"
        button = tk.Button(internal_frame, text="Cerrar ventana", command=lambda: cerrar(internal_frame, tabla, tab))
        button.pack(pady=10)
    else:
        messagebox.showinfo("info", "Cierre el modelo actual para abrir otro")


def poissonV(ventana,tabla,tabla_numeros, resultadoBondad , tab):
    global is_open
    if not is_open:
        is_open = True
        # Crear un frame para la "ventana interna"
        internal_frame = tk.Frame(ventana, bg="#7FFFD4", bd=2, relief=tk.RIDGE)
        # Ubicar el frame en el centro de la pantalla
        internal_frame.grid(row=2, column=1)

        titulo_p = tk.Label(internal_frame, text="Poisson", font=("Arial", 16, "bold"), bg="white")
        titulo_p.pack()

        # etiqueta de texto
        label1 = tk.Label(internal_frame, text="Cantidad de numeros a generar", bg="white")
        label1.pack()

        # para cargar numero
        numerosGenerar = tk.Entry(internal_frame)
        numerosGenerar.pack()

        # etiqueta de texto
        label2 = tk.Label(internal_frame, text="Ingresar Media:", bg="white")
        label2.pack()

        # para cargar numero
        media = tk.Entry(internal_frame)
        media.pack()


        # es un boton        v            texto a mostrar                   fun que necesita parametros
        boton = tk.Button(internal_frame, text="Calcular", command=lambda: distribuciones.poisson(float(media.get()),
                                                                                                  int(numerosGenerar.get()),
                                                                                                  tabla,tabla_numeros ,resultadoBondad))
        boton.pack()

        # Agregar un botón en la "ventana interna"
        button = tk.Button(internal_frame, text="Cerrar ventana", command=lambda: cerrar(internal_frame,tabla,tab))
        button.pack(pady=10)
    else:
        messagebox.showinfo("info", "Cierre el modelo actual para abrir otro")


def normalV(ventana, tabla, tabla_numeros, resultadoBondad, tab):
    global is_open
    if not is_open:
        is_open = True
        # Crear un frame para la "ventana interna"
        internal_frame = tk.Frame(ventana, bg="white", bd=2, relief=tk.RIDGE)

        # Ubicar el frame en el centro de la pantalla
        internal_frame.grid(row=2, column=1)

        titulo_n = tk.Label(internal_frame, text="Normal", font=("Arial", 16, "bold"), bg="white")
        titulo_n.pack()

        # etiqueta de texto
        label1 = tk.Label(internal_frame, text="Cantidad de numeros a generar", bg="white")
        label1.pack()

        # para cargar numero
        numeros_a_generar = tk.Entry(internal_frame)
        numeros_a_generar.pack()

        # etiqueta de texto
        txt_media = tk.Label(internal_frame, text="Ingresar Media:", bg="white")
        txt_media.pack()

        # para cargar numero
        media = tk.Entry(internal_frame)
        media.pack()

        # etiqueta de texto
        txt_de = tk.Label(internal_frame, text="Ingresar De:", bg="white")
        txt_de.pack()

        # para cargar numero
        de = tk.Entry(internal_frame)
        de.pack()

        # cantidad de intervalos adsasdasd
        res = tk.Label(internal_frame, text="Ingrese Cantidad de intervalos", bg="white")
        res.pack()
        interv = tk.Entry(internal_frame)
        interv.pack()

        # Seleccionar una opción por defecto
        opcion_seleccionada = tk.StringVar(value="1")
        global select2
        select2 = "1"

        def imprimir_opcion():
            global select2
            select2 = str(opcion_seleccionada.get())

        # Función para cambiar la opción seleccionada
        def cambiar_opcion(opcion):
            opcion_seleccionada.set(opcion)

        # Crear los botones de selección
        opcion1 = tk.Radiobutton(internal_frame, text="Box Muller", variable=opcion_seleccionada, value="1",
                                 command=imprimir_opcion)
        opcion2 = tk.Radiobutton(internal_frame, text="Convoluciòn", variable=opcion_seleccionada, value="2",
                                 command=imprimir_opcion)
        # Empaquetar los botones en la ventana
        opcion1.pack()
        opcion2.pack()


        # es un boton        v               texto a mostrar                   fun que necesita parametros
        boton = tk.Button(internal_frame, text="Calcular", command=lambda: distribuciones.normal(
            int(numeros_a_generar.get()),
            float(media.get()),
            float(de.get()),
            int(interv.get()), tabla,tabla_numeros,resultadoBondad,select2))
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
    tabla.heading(column="#0", text="", anchor='w')
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
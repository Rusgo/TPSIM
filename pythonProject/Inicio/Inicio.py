import tkinter as tk
from tkinter import ttk
import ventanas
from PIL import Image, ImageTk


# metodo para asignar la ventana al frame
def abrir():
    if combo.get() == "Uniforme":
        ventanas.uniformeV(ventana, tablachi, tabla_numeros,resultadoBondad, tabla_numeros )
    elif combo.get() == "Exponencial":
        ventanas.exponencialV(ventana, tablachi,tabla_numeros,resultadoBondad, tabla_numeros )
    elif combo.get() == "Poisson":
        ventanas.poissonV(ventana, tablachi, tabla_numeros, resultadoBondad, tabla_numeros )
    elif combo.get() == "Normal":
        ventanas.normalV(ventana, tablachi, tabla_numeros,resultadoBondad, tabla_numeros )


if __name__ == '__main__':
    # ventana creada
    ventana = tk.Tk()
    ventana.title("Inicio")
    ventana.configure(bg="white")
    ventana.geometry("1920x1080+10+10")
    ventana.configure()

    # creamos las columnas y filas
    ventana.columnconfigure(0, weight=10)
    ventana.columnconfigure(1, weight=10)
    ventana.columnconfigure(2, weight=10)
    ventana.columnconfigure(3, weight=40)
    ventana.columnconfigure(4, weight=30)
    ventana.rowconfigure(0, weight=25)
    ventana.rowconfigure(1, weight=5)
    ventana.rowconfigure(2, weight=70)


    '''# crea el canvas
    canvas = tk.Canvas(ventana, width=300, height=200)
    canvas.grid(row=0, column=0, sticky='nsew', columnspan=5, rowspan=3)

    # crea un rectángulo con un gradiente de color
    canvas.create_rectangle(0, 0, 1980, 1080, fill='', outline='white')
    num_lines = 1080
    for i in range(num_lines):
        r = hex(i * 255 // num_lines)[2:].zfill(2)
        g = hex(255 - i * 255 // num_lines)[2:].zfill(2)
        color = '#' + r + g + '00'
        canvas.create_line(0, i, 1920, i, fill=color, width=1)'''

    # ajusta el tamaño del canvas a la ventana
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=1)

    # titulo
    titulo = tk.Label(ventana, text="Trabajo Practico Nro 1.", font=("Arial", 16, "bold"), bg="white", justify="left")
    titulo.grid(row=0, columnspan=3)
    # etiqueta de texto
    label2 = tk.Label(ventana, text="Modelo", bg="white")
    label2.grid(row=1, column=0)
    # opc del combo
    opciones = ["Uniforme", "Normal", "Exponencial", "Poisson"]
    # Crear el Combobox
    combo = ttk.Combobox(ventana, values=opciones)
    combo.state(["readonly"])
    combo.grid(row=1, column=1)
    # Establecer el valor predeterminado
    combo.set("Seleccione una opción")
    # es un boton
    boton = tk.Button(ventana, text="Abrir", command=abrir)
    boton.grid(row=1, column=2)

    titulo_bondad = tk.Label(ventana, text="Numeros Generados:", bg="white", )
    titulo_bondad.grid(row=0, column=3)

    tabla_numeros = ttk.Treeview(ventana, columns=("1"))
    tabla_numeros.grid(column=3, row=1)

    #tabla chi cuadr
    tablachi = ttk.Treeview(ventana, columns=[str(i) for i in range(9)])
    for i in range(9):
        tablachi.heading(i, text="")
        tablachi.column(i, width=100)
    tablachi.grid(row=2, column=3, columnspan=2, rowspan=2)
    titulo_bondad = tk.Label(ventana, text="Prueba bondad de Ajuste:", bg="white", justify="left")
    titulo_bondad.grid(row=1, column=3, rowspan=2)
    resultadoBondad = ""

    # ventana iniciada
    ventana.mainloop()



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ventanas


# metodo para asignar la ventana al frame
def abrir():
    if combo.get() == "Uniforme":
        ventanas.uniformeV(ventana, tablachi)
    elif combo.get() == "Exponencial":
        ventanas.exponencialV(ventana, tablachi)
    elif combo.get() == "Poisson":
        ventanas.poissonV(ventana, tablachi)
    elif combo.get() == "Normal":
        ventanas.normalV(ventana, tablachi)


if __name__ == '__main__':
    # ventana creada
    ventana = tk.Tk()
    ventana.title("Inicio")
    ventana.configure(bg="white")
    ventana.geometry("1980x1080+10+10")
    # creamos las columnas y filas
    ventana.columnconfigure(0, weight=30)
    ventana.columnconfigure(1, weight=40)
    ventana.columnconfigure(2, weight=30)
    ventana.rowconfigure(0, weight=10)
    ventana.rowconfigure(1, weight=10)
    ventana.rowconfigure(2, weight=80)
    # titulo
    titulo = tk.Label(ventana, text="Trabajo Practico Nro 1.", font=("Arial", 16, "bold"))
    titulo.grid(row=0, columnspan=3)
    # etiqueta de texto
    label2 = tk.Label(ventana, text="Modelo")
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

    #tabla chi cuadrado
    tablachi = ttk.Treeview(ventana, columns=("Desde-Hasta","Fo","fe","c", "cAcu"))
    tablachi.grid(row=2, column=3)

    cerrado = tk.Label(ventana, text="")
    tablachi.grid(row=2, column=4)

    # ventana iniciada
    ventana.mainloop()
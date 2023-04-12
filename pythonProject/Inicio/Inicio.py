import tkinter as tk
from tkinter import ttk
import random
import time
import pandas as pd
import cosas

import ventanas

from cosas.graficador import graficar


#metodo para asignar la ventana al frame
def abrir():
    if combo.get() == "Uniforme":
        ventanas.uniformeV(ventana)
    elif combo.get() == "Exponencial":
        ventanas.exponencialV(ventana)
    elif combo.get() == "Poisson":
        ventanas.poissonV(ventana)
    elif combo.get() == "Normal":
        pass


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
    ventana.rowconfigure(0, weight=30)
    ventana.rowconfigure(1, weight=70)

    # etiqueta de texto
    label2 = tk.Label(ventana, text="Modelo")
    label2.grid(row=0, column=0)

    #opc del combo
    opciones = ["Uniforme", "Normal", "Exponencial", "Poisson"]

    # Crear el Combobox
    combo = ttk.Combobox(ventana, values=opciones)
    combo.state(["readonly"])
    combo.grid(row=0, column=1)


    # Establecer el valor predeterminado
    combo.set("Seleccione una opción")


    #es un boton
    boton = tk.Button(ventana, text="Abrir", command=abrir)
    boton.grid(row=0, column=2)



    # ventana iniciada
    ventana.mainloop()
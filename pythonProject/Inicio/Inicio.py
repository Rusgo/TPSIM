import tkinter as tk
from tkinter import ttk
import ventanas


# metodo para asignar la ventana al frame
def abrir():
    if combo.get() == "Uniforme":
        ventanas.uniformeV(ventana, tablachi,tabla_numeros,resultadoBondad,tabla_numeros )
    elif combo.get() == "Exponencial":
        ventanas.exponencialV(ventana, tablachi,tabla_numeros,resultadoBondad,tabla_numeros )
    elif combo.get() == "Poisson":
        ventanas.poissonV(ventana, tablachi,tabla_numeros,resultadoBondad,tabla_numeros )
    elif combo.get() == "Normal":
        ventanas.normalV(ventana, tablachi,tabla_numeros,resultadoBondad,tabla_numeros )


if __name__ == '__main__':
    # ventana creada
    ventana = tk.Tk()
    ventana.title("Inicio")
    ventana.configure(bg="white")
    ventana.geometry("1980x1080+10+10")
    ventana.configure()
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

    tabla_numeros = ttk.Treeview(ventana, columns=("1"))
    tabla_numeros.grid(column=4,row=1)

    #tabla chi cuadr
    tablachi = ttk.Treeview(ventana, columns=[str(i) for i in range(9)])
    for i in range(9):
        tablachi.heading(i, text="")
        tablachi.column(i, width=100)
    tablachi.grid(row=1, column=3, columnspan=2, rowspan=2)
    tablachi.grid(row=1, column=3, columnspan=2, rowspan=2)




    resultadoBondad = tk.Label(ventana, text="")



    # ventana iniciada
    ventana.mainloop()



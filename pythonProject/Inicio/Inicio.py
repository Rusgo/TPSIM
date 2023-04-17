import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from scipy.stats import chi2

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


def testChi(error):
    res = tablachi.get_children()
    ult = res[-1]
    valores_ultima_fila = tablachi.item(ult, 'values')
    chiacu = float(valores_ultima_fila[4])
    print(len(res)-3)
    valor_p = 1 - chi2.cdf(chiacu, len(res)-3)
    nivel_de_significancia = 0.1  # nivel de significancia deseado, por ejemplo 0.05 para un nivel de confianza del 95%

    print("------------------------------------------------------")
    if valor_p < error:
        print("Se rechaza la hipótesis nula.")
    else:
        print("No se puede rechazar la hipótesis nula.")


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

    #tabla chi cuadr
    tablachi = ttk.Treeview(ventana, columns=[str(i) for i in range(9)])
    for i in range(9):
        tablachi.heading(i, text="")
        tablachi.column(i, width=100)
    tablachi.grid(row=2, column=3)

    tablachi.grid(row=2, column=4)

    '''
    errores = ["0.1","0.05", "0.025"]
    error = ttk.Combobox(ventana, values=errores)
    error.grid(row=1, column=4)

    tabulado = tk.Button(ventana, text="calcular tabulado" , command=lambda: testChi(float(error.get())))
    tabulado.grid(row=1, column=5)
    '''

    # ventana iniciada
    ventana.mainloop()



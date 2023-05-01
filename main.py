# This is a sample Python scrip
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from montecarlo import inicio
import tkinter as tk
import tkinter.ttk as tkk


if __name__ == '__main__':

    # VENTANA DE INICIO

    ventana = tk.Tk()
    ventana.title("Inicio")
    ventana.configure(bg="white")
    ventana.geometry("1920x1080+10+10")

    # LABELS & INPUTS
    titulo_horas = tk.Label(ventana, text="Ingrese cantidad de horas a simulas:", background="white")
    titulo_horas.pack()
    txt_horas = tk.Entry(ventana)
    txt_horas.pack()

    titulo_media = tk.Label(ventana, text="Ingresar Media de casas llamadas por hora:", background="white")
    titulo_media.pack()
    txt_media = tk.Entry(ventana)
    txt_media.pack()

    titulo_de = tk.Label(ventana, text="Ingresar desviacion estandar:", background="white")
    titulo_de.pack()
    txt_de = tk.Entry(ventana)
    txt_de.pack()

    titulo_desde = tk.Label(ventana, text="Ingresar el Nro de Hora desde la que desea ver Información:", background="white")
    titulo_desde.pack()
    txt_desde = tk.Entry(ventana)
    txt_desde.pack()

    # BTN SIMULAR
    btn_simular = tk.Button(ventana, text="Simular", command=lambda: inicio(float(txt_media.get()), float(txt_de.get()),
                                                                            int(txt_horas.get()), int(txt_desde.get()),
                                                                            tablaintervalo, tablaf))
    btn_simular.pack()

    # TABLAS
    columnas = ["Nro Hora", "Nro Llamada", "RND Atiende", "Atiende SI/NO", "RND Género", "Género", "RND Compra",
                "Compra SI/NO", "RND Gasto", "Dinero Gastado", "Cantidad de Atendidos", "Cantidad de Ventas",
                "Cantidad de Hombres", "Gastos de Hombres", "Cantidad de Mujeres", "Gastos de Mujeres",
                "Monto Recaudado"]
    tablaintervalo = tkk.Treeview(ventana, columns=[str(i) for i in range(17)], height=30)
    tablaf = tkk.Treeview(ventana, columns=[str(i) for i in range(17)], height=5)
    for col, nombre_columna in enumerate(columnas):
        tablaintervalo.column(column=col, width=100, minwidth=50, anchor='w')
        tablaintervalo.heading(column=col, text=nombre_columna, anchor='w')
        tablaf.column(column=col, width=100, minwidth=50, anchor='w')
        tablaf.heading(column=col, text=nombre_columna, anchor='w')
    tablaintervalo.pack()
    titulo_final = tk.Label(ventana, text="Ultima fila:")
    titulo_final.pack()
    tablaf.pack()

    ventana.mainloop()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

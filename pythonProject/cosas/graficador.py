import matplotlib.pyplot as plt


# Realiza los calculos necesarios para hacer el grafico y los muestra
def graficar(n, min, max, table):
    clases = int(pow(n, 1/2))
    ancho = (max-min)/clases
    desde = min
    hasta = desde + ancho
    x = []
    y = []
    c = 0
    x.append(str(round(desde)) + "-" + str(round(hasta)))
    # lo podemos hacer antes
    for item in table.get_children():
        valor = float(table.item(item)["values"][0])
        if desde <= valor < hasta:
            c += 1
        elif hasta <= valor:
            y.append(c)
            c = 1
            desde = hasta
            hasta = desde + ancho
            x.append(str(round(desde)) + "-" + str(round(hasta)))
    y.append(c)

    # Crear el gráfico de barras
    plt.bar(x, y)

    # Añadir etiquetas y título
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.title('Ejemplo de gráfico de barras')

    # Mostrar el gráfico
    plt.show()

    # Guardar el gráfico en un archivo
    plt.savefig('grafico.png')
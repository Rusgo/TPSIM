import matplotlib.pyplot as plt


# Realiza los cálculos necesarios para hacer el grafico y los muestra
def graficar(n, min, max, listan_numeros, clases, distri):
    # clases = int(pow(n, 1/2))
    ancho = (max-min)/clases
    desde = min
    hasta = desde + ancho
    x = []
    y = []
    c = 0
    x.append(str(round(desde, 2)) + "-" + str(round(hasta, 2)))
    for numero in listan_numeros:
        valor = numero
        if desde <= valor < hasta:
            c += 1
        elif hasta <= valor < (hasta + ancho) and valor != max:
            y.append(c)
            c = 1
            desde = hasta
            hasta = desde + ancho
            x.append(str(round(desde, 2)) + "-" + str(round(hasta, 2)))
        elif valor >= (hasta + ancho) and valor != max:
            y.append(c)
            intervalos_salteados = int(round((valor - hasta) / ancho))
            for i in range(intervalos_salteados):
                y.append(0)
                desde = hasta
                hasta = desde + ancho
                x.append(str(round(desde, 2)) + "-" + str(round(hasta, 2)))
            c = 1
            desde = hasta
            hasta = desde + ancho
            x.append(str(round(desde, 2)) + "-" + str(round(hasta, 2)))
        elif valor == max:
            c += 1

    y.append(c)

    # Crear el gráfico de barras
    plt.bar(x, y)

    # Añadir etiquetas y título
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia Observada')
    plt.title(distri)

    # Mostrar el gráfico
    plt.show()

    # Guardar el gráfico en un archivo
    plt.savefig('grafico.png')


def graficar_poisson(n, min, max, listan_numeros, distri):
    # clases = int(pow(n, 1/2))

    lista_filtrada = list(set(listan_numeros))
    x = []
    y = []
    for numero in lista_filtrada:
        x.append(numero)
        y.append(listan_numeros.count(numero))

    # Crear el gráfico de barras
    plt.bar(x, y)

    # Añadir etiquetas y título
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia Observada')
    plt.title(distri)

    # Mostrar el gráfico
    plt.show()

    # Guardar el gráfico en un archivo
    plt.savefig('grafico.png')
import math
from scipy.stats import chi2
import Inicio
from Inicio import ventanas
import distribuciones

def chicuad(n, min, max, listan_numeros, clases, lambd, media, de, funprob, tabla):
    Inicio.ventanas.preparar_tabla_chi(tabla)
    clases = int(pow(n, 1/2))
    ancho = (max - min) / clases
    desde = min
    hasta = desde + ancho
    chiacu = 0
    fo = 0

    for numero in listan_numeros:
        valor = numero
        if desde <= valor < hasta:
            fo += 1
        elif hasta <= valor:
            # hacemos calculo de probabilidad si acuEsperada no llega a 5 no cerramos el intervalo, calculamos c y lo
            # ponemos en la tabla
            prob, grados_de_libertad = tipo(funprob, lambd, desde, hasta, clases, media, de)
            # agrego cosas a la tabla
            fe = prob * n

            if fe >= 5:
                intervalo = str(round(desde, 2)) + "-" + str(round(hasta, 2))
                chi = pow((fo-fe), 2)/fe
                chiacu += chi
                # desp de cargartodo a la tabla hacer fo 0
                tabla.insert(parent='', index='end', values=(intervalo, fo, fe, chi, chiacu))
                fo = 1
                desde = hasta
                hasta = desde + ancho
            else:
                hasta += ancho
                fo += 1
    prob, grados_de_libertad = tipo(funprob, lambd, desde, hasta, clases, media, de)

    fe = prob*n

    hasta += ancho

    if fe >= 5:
        tabla.insert(parent='', index='end', values=(intervalo, fo, fe, chi, chiacu))
    else:
        # last_row_index = tabla.index(tabla.get_children()[-1])
        # res = tabla.item(last_row_index, 'values')
        res = tabla.get_children()
        ult = res[-1]
        valores_ultima_fila = tabla.item(ult, 'values')
        fe = float(valores_ultima_fila[2]) + fe
        fo = float(valores_ultima_fila[1]) + fo
        chi = pow((fo-fe), 2)/fe
        chiacu = chi + float(valores_ultima_fila[4])
        dh = valores_ultima_fila[0].split("-")
        intervalo = dh[0] + "-" + str(ancho)
        tabla.delete(ult)
        tabla.insert(parent='', index='end', values=(intervalo, fo, fe, chi, chiacu))

    valor_p = 1 - chi2.cdf(chiacu, grados_de_libertad)

    nivel_de_significancia = 0.05  # nivel de significancia deseado, por ejemplo 0.05 para un nivel de confianza del 95%

    if valor_p < nivel_de_significancia:
        print("Se rechaza la hipótesis nula.")
    else:
        print("No se puede rechazar la hipótesis nula.")




def ks(n, min, max, listan_numeros, clases, lambd, media, de, funprob, tabla):  # ver si funciona posta o da cualquier verdurta

    # cambio el nombre a las columnas por los del metodo ks lo podemos pasar aparte y hacer un if para poner el encabezado de ks o chi cuadrado
    Inicio.ventanas.preparar_tabla_ks(tabla)

    clases = int(pow(n, 1/2))
    ancho = (max - min) / clases
    desde = min
    hasta = desde + ancho
    x = []
    y = []
    fo = 0
    ks = 0
    res = 0
    maximo = 0
    pe_acu = 0  # acumulamos el valor de pe
    po_acu = 0  # acumulamos evalor de po

    for numero in listan_numeros:
        valor = numero
        if desde <= valor < hasta:
            fo += 1
        elif hasta <= valor != max:
            pe, grados_de_libertad = tipo(funprob, lambd, desde, hasta, clases, media, de) # los if repetidos 20 veces en un metodo
            x = (str(round(desde, 2)) + "-" + str(round(hasta, 2)))
            # calculamos lo necesario para obtener el resultado de la ks
            pe_acu += pe
            po = fo/n
            po_acu += po

            res = abs(pe_acu-po_acu)
            if res > maximo:
                maximo = res

            tabla.insert(parent='', index='end', values=(x, fo, str(pe*n), po, pe, po_acu, pe_acu, res, maximo))
            fo = 1

            desde = hasta
            hasta = desde + ancho

        elif valor == max:
            fo += 1

    desde = hasta
    hasta = desde + ancho

    pe, grados_de_libertad = tipo(funprob, lambd, desde, hasta, clases, media, de)

    pe_acu += pe
    po = fo / n
    po_acu += po

    res = abs(pe_acu - po_acu)
    if res > maximo:
        maximo = res

    tabla.insert(parent='', index='end', values=(x, fo, str(pe*n), po, pe, po_acu, pe_acu, res, maximo))


def calculo(n, min, max, listan_numeros, clases, lambd, media, de, funprob, tabla):
    if n <= 30:
        ks(n, min, max, listan_numeros, clases, lambd, media, de, funprob, tabla)
    else:
        chicuad(n, min, max, listan_numeros, clases, lambd, media, de, funprob, tabla)


def tipo(funprob, lambd, desde, hasta, clases, media, de):
    if funprob == 0:
        pe = 1/clases
        grados_de_libertad = clases - 0 - 1  # número de grados de libertad
    elif funprob == 1:
        pe = distribuciones.probExponencial(lambd, (desde + hasta) / 2, desde, hasta)
        grados_de_libertad = clases - 1 - 1  # número de grados de libertad
    elif funprob == 2:
        pe = distribuciones.probPoisson()
    elif funprob == 3:
        pe = distribuciones.probNormal((desde + hasta) / 2, media, de, hasta, desde)
        grados_de_libertad = clases - 2 - 1  # número de grados de libertad
    return pe, grados_de_libertad


def chi_poisson(n, lista, lambd, tabla):
    x = list(set(lista))
    x_agrupado = []
    fo = 0
    string = ""
    c = 0
    c_acu = 0
    for numero in x:
        string += str(numero)
        fo = lista.count(numero)
        prob = distribuciones.probPoisson(lambd, numero)
        fe = prob*n

        if fe >= 5:
            c = pow((fe-fo), 2)/fe
            c_acu += c
            # todo esto a la tabla
            tabla.insert(parent='', index='end', values=(string, fo, fe, c, c_acu))
            string = "" # reseteo el string y a otro numero
        elif numero != x[-1]:
            string += ";"
        else:
            res = tabla.get_children()
            ult = res[-1]

            valores_ultima_fila = tabla.item(ult, 'values')

            fe = float(valores_ultima_fila[2]) + fe
            fo = float(valores_ultima_fila[1]) + fo
            chi = pow((fo - fe), 2) / fe
            chiacu = chi + float(valores_ultima_fila[4])
            intervalo = valores_ultima_fila[0]
            tabla.delete(ult)
            tabla.insert(parent='', index='end', values=(intervalo, fo, fe, chi, chiacu))







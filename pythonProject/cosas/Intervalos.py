import math


def chicuad(n, min, max, listan_numeros, clases, lambd, media, de, funprob, tabla):
    clases = int(pow(len(listan_numeros), 1/2))
    ancho = (max - min) / clases
    desde = min
    hasta = desde + ancho
    chiacu = 0
    acuEsperada = 0
    fo = 0
    for numero in listan_numeros:
        valor = numero
        if desde <= valor < hasta:
            fo += 1
        elif hasta <= valor:
            # hacemos calculo de probabilidad si acuEsperada no llega a 5 no cerramos el intervalo, calculamos c y lo
            # ponemos en la tabla
            if funprob == 0:
                prob = probUniforme(n, clases)
            elif funprob == 1:
                prob = probExponencial(lambd, (desde+hasta)/2, desde, hasta)
            elif funprob == 2:
                prob = probPoisson()
            elif funprob == 3:
                prob = probNormal((desde+hasta)/2, media, de, hasta, desde)

            fe = prob * len(listan_numeros)

            # agrego cosas a la tabla
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
    if funprob == 0:
        prob = probUniforme(n, clases)
    elif funprob == 1:
        prob = probExponencial(lambd, (desde + hasta) / 2, desde, hasta)
    elif funprob == 2:
        prob = probPoisson()
    elif funprob == 3:
        prob = probNormal((desde + hasta) / 2, media, de, hasta, desde)

    fe = prob * len(listan_numeros)
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
        tabla.insert(parent='', index='end',values=(intervalo, fo, fe, chi, chiacu))


# calculos de probabilidad de cada distrib
def probNormal(marca, media, de, hasta,desde):
    res = ((math.exp((-0.5)*(pow(((marca-media)/de), 2))))/(de*math.sqrt(2*math.pi)))*(hasta-desde)
    return res


def probPoisson():
    pass

def probExponencial(lambd, marca, desde,hasta):
    res = (lambd*math.exp(-lambd*marca)) * (hasta - desde)
    return res


def probUniforme(n, clases):
    return round(n/clases)
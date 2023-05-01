import normal
import random


class Registro:
    def __init__(self):
        self.hombres_c = 0
        self.hombres_gastos = 0
        self.mujeres_c = 0
        self.mujeres_gastos = 0
        self.ventas_c = 0
        self.atendidos_c = 0
        self.ingreso_total = 0
        self.nro_llamada = 0


def inicio(media, de, horas, desde, tablaintervalo, tablafinal):
    tablaintervalo.delete(*tablaintervalo.get_children())
    tablafinal.delete(*tablafinal.get_children())
    llamada_actual = []
    llamada_anterior = []
    con_acu = Registro()
    hasta = desde + 500
    primera_fila = []
    ultima_fila = []
    res = ["-"]*8
    a = ["rnda", "a", "rndg", "g", "rndcombra", "si/no", "rndg", "gasto"]
    for i in range(horas):
        if i % 2 == 0:
            n1, n2 = normal.normal(media, de)
            for j in range(int(n1)):
                con_acu.nro_llamada += 1
                res = montecarlo(con_acu)
                llamada_anterior = llamada_actual
                llamada_actual = [str(i+1), con_acu.nro_llamada, res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7]
                                  , con_acu.atendidos_c, con_acu.ventas_c, con_acu.hombres_c, con_acu.hombres_gastos,
                                  con_acu.mujeres_c, con_acu.mujeres_gastos, con_acu.ingreso_total]
                if desde <= con_acu.nro_llamada <= hasta:
                    tablaintervalo.insert(parent='', index='end', values=llamada_actual)
        else:
            for j in range(int(n2)):
                con_acu.nro_llamada += 1
                res = montecarlo(con_acu)
                llamada_anterior = llamada_actual
                llamada_actual = [str(i+1), con_acu.nro_llamada, res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7]
                                  , con_acu.atendidos_c, con_acu.ventas_c, con_acu.hombres_c, con_acu.hombres_gastos,
                                  con_acu.mujeres_c, con_acu.mujeres_gastos, con_acu.ingreso_total]
                if desde <= con_acu.nro_llamada <= hasta:
                    tablaintervalo.insert(parent='', index='end', values=llamada_actual)
    tablafinal.insert(parent='', index='end',values=llamada_actual)


def montecarlo(reg):
    resultado = ["-"]*8  # ["rnda", "a", "rndg", "g", "rndcombra", "si/no", "rndg", "gasto"]
    atiende_var, resultado[0] = atiende()
    if atiende_var:
        reg.atendidos_c += 1
        resultado[1] = "Atiende"
        genero_var, resultado[2] = genero()
        if genero_var:
            resultado[3] = "Hombre"
            reg.hombres_c += 1
            comprah_var, resultado[4] = compraH()
            if comprah_var:
                resultado[5] = "si"
                monto_vendido, resultado[6] = gastoH()
                resultado[7] = monto_vendido
                reg.ventas_c += 1
                reg.ingreso_total += monto_vendido
                reg.hombres_gastos += monto_vendido
            else:
                resultado[5] = "no"
        else:
            resultado[3] = "Mujer"
            compram_var, resultado[4] = compraM()
            if compram_var:
                resultado[5] = "si"
                reg.mujeres_c += 1
                monto_vendido, resultado[6] = gastoM()
                resultado[7] = monto_vendido
                reg.ventas_c += 1
                reg.ingreso_total += monto_vendido
                reg.mujeres_gastos += monto_vendido
            else:
                resultado[5] = "no"
    else:
        resultado[1] = "No atiende"
    return resultado


def atiende():
    rnd = random.random()
    if rnd < 0.15:
        return False, rnd
    else:
        return True, rnd


def genero():
    rnd = random.random()
    if rnd < 0.2:
        return True, rnd #Hombre
    else:
        return False, rnd #Mujer

def compraH():
    rnd = random.random()
    if rnd < 0.4:
        return True, rnd
    else:
        return False, rnd


def compraM():
    rnd = random.random()
    if rnd < 0.7:
        return True, rnd
    else:
        return False, rnd


def gastoH():
    rnd = random.random()
    if rnd < 0.05:
        return 5, rnd
    elif rnd < 0.25:
        return 10, rnd
    elif rnd < 0.60:
        return 15, rnd
    else:
        return 25, rnd


def gastoM():
    rnd = random.random()
    if rnd < 0.2:
        return 5, rnd
    elif rnd < 0.8:
        return 10, rnd
    elif rnd < 0.95:
        return 15, rnd
    else:
        return 25, rnd

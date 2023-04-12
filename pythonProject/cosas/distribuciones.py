import random
import time
import math
from cosas.graficador import graficar


# realiza los calculos necesarios para pasar un numero a una distrib uniforme y las guarda en una tabla
def uniforme(n, a, b, table):
    table.delete(*table.get_children())
    start_time = time.time()  # Registrar el tiempo actual
    randoms = sorted(generarNums(n))
    for i in range(n):
        res = numUniforme(randoms[i], a, b)
        table.insert("", "end", values=(str(res)))

    end_time = time.time()  # Registrar el tiempo actual nuevamente

    execution_time = end_time - start_time  # Calcular el tiempo de ejecución

    print("La función tardó {} segundos en ejecutarse.".format(execution_time))
    graficar(n, a, b, table)


# lo mismo que arriba pero con otra distrib
def exponencial(n, media, table):
    table.delete(*table.get_children())
    start_time = time.time()  # Registrar el tiempo actual
    numeros = sorted(generarNums(n))
    min_v = numExponencial(numeros[0], media)
    max_v = numExponencial(numeros[-1], media)
    for i in range(n):
        res = numExponencial(numeros[i], media)
        table.insert("", "end", values=(str(res)))

    graficar(n, min_v, max_v, table)
    end_time = time.time()  # Registrar el tiempo actual nuevamente

    execution_time = end_time - start_time  # Calcular el tiempo de ejecución

    print("La función tardó {} segundos en ejecutarse.".format(execution_time))


def numUniforme(valor, a, b):
    uni = valor * (b - a) + a
    return uni


def numExponencial(numero, media):
    exp = (-media * math.log(1 - numero))
    return exp


def generarNums(n):
    nums = []
    for i in range(n):
        num = random.random()
        nums.append(num)
    return nums


def poisson(lamd, n, table):
    table.delete(*table.get_children())
    z = []
    for i in range(n):
        p = 1
        x = -1
        a = math.exp(-lamd)
        while p >= a:
            u = random.random()
            p = p * u
            x = x + 1
        z.append(x)
    z = sorted(z)
    for i in range(len(z)):
        table.insert("", "end", values=(str(z[i])))
    graficar(n, z[0], z[-1], table)






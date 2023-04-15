import random
import time
import math
from cosas import Intervalos
from cosas.graficador import graficar


# realiza los calculos necesarios para pasar un numero a una distrib uniforme y las guarda en una tabla
def uniforme(n, a, b, clases, tabla):
    tabla.delete(*tabla.get_children())
    randoms = sorted(generarNums(n))
    for i in range(n):
        res = numUniforme(randoms[i], a, b)
        randoms[i] = res
    Intervalos.chicuad(n, randoms[0], randoms[-1], randoms, clases, False, False, False, 0, tabla)
    graficar(n, randoms[0], randoms[-1], randoms, clases, "Uniforme")


def numUniforme(valor, a, b):
    uni = valor * (b - a) + a
    return uni


# lo mismo que arriba pero con otra distrib
def exponencial(n, media, clases, tabla):
    tabla.delete(*tabla.get_children())
    numeros = sorted(generarNums(n))
    for i in range(n):
        numeros[i] = numExponencial(numeros[i], media)
    Intervalos.chicuad(n, numeros[0], numeros[-1], numeros, clases, 1/media, False, False, 1, tabla)
    graficar(n, numeros[0], numeros[-1], numeros, clases, "Exponencial")


def numExponencial(numero, media):
    exp = (-media * math.log(1 - numero))
    return exp


# Usamos algoritmo dado por el profesor y lo utilizamos las veces deseadas por el profesor
def poisson(lamd, n, clases, tabla):
    tabla.delete(*tabla.get_children())
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
    graficar(n, z[0], z[-1], z, clases, "Poisson")


# usamos el metodo box muller para obtener los numero, alternamos n1 y n2 segun si es par i o no
def normal(n, media, de, clases, tabla):
    tabla.delete(*tabla.get_children())
    numeros_random = []
    for i in range(n):
        rnd1 = generarNums(1)
        rnd2 = generarNums(1)
        if (i % 2) == 0:
            n1 = (pow(-2*math.log(rnd1[0]), 1/2) * math.cos(2*math.pi*rnd2[0]))*de+media
            numeros_random.append(n1)
        else:
            n2 = (pow(-2*math.log(rnd1[0]), 1/2) * math.sin(2*math.pi*rnd2[0]))*de+media
            numeros_random.append(n2)
    numeros_random = sorted(numeros_random)
    # lo comentado es de testeo
    # cambiar = [1.56, 2.21, 3.15, 4.61, 4.18, 5.20, 4.87, 7.71, 5.15, 6.76, 7.28, 4.23, 3.54, 2.75, 4.69, 5.86, 6.25, 4.27, 4.91, 4.78, 2.46, 3.97, 6.09, 6.19, 4.20, 3.48, 5.83, 6.36, 5.90, 5.43, 3.87, 2.21, 3.74, 4.61, 4.18, 5.20, 4.28, 7.71, 5.15, 6.76, 7.28, 4.23, 3.21, 2.75, 4.69, 5.86, 6.25, 4.27, 4.91, 4.78]
    # cambiar.sort()
    #Intervalos.chicuad(n, cambiar[0], cambiar[-1], cambiar, clases, False, 4.7962, 1.4598279, 3, tabla)
    Intervalos.chicuad(n, numeros_random[0], numeros_random[-1], numeros_random, clases, False, media, de, 3, tabla)
    graficar(n, numeros_random[0], numeros_random[-1], numeros_random, clases, "Normal")

def generarNums(n):
    nums = []
    for i in range(n):
        num = random.random()
        nums.append(num)
    return nums





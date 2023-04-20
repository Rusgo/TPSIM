import random
import time
import math
import Pruebas_Bondad
from graficador import graficar, graficar_poisson
import tkinter as tk
from tkinter import ttk, messagebox


# realiza los calculos necesarios para pasar un numero a una distrib uniforme y las guarda en una tabla
def uniforme(n, a, b, clases, tabla, tabla_numeros, resultadoBondad):
    tabla.delete(*tabla.get_children())
    tabla_numeros.delete(*tabla_numeros.get_children())
    if n <= 50000:
        if a < b:
            tabla_numeros.column(column="#0", width=100, minwidth=50, anchor='w')
            tabla_numeros.heading(column="#0", text="Numeros Generados", anchor='w')
            randoms = sorted(generarNums(n))
            for i in range(n):
                res = numUniforme(randoms[i], a, b)
                randoms[i] = res
                tabla_numeros.insert(parent='', index='end', values=str(res))
            Pruebas_Bondad.calculo(n, randoms[0], randoms[-1], randoms, clases, False, False, False, 0, tabla,
                                   resultadoBondad)
            graficar(n, randoms[0], randoms[-1], randoms, clases, "Uniforme")
        else:
            messagebox.showinfo("info", "Ingrese un límite superior mayor al inferior")
    else:
        messagebox.showinfo("Info", "Ingrese una cantidad menor o igual a 50000")


def numUniforme(valor, a, b):
    uni = valor * (b - a) + a
    return uni


# lo mismo que arriba pero con otra distrib
def exponencial(n, media, clases, tabla,tabla_numeros,resultadoBondad, selec):
    tabla.delete(*tabla.get_children())
    tabla_numeros.delete(*tabla_numeros.get_children())
    if n <= 50000:
        if selec == "lambda":
            media = 1/media
        tabla_numeros.column(column="#0", width=100, minwidth=50, anchor='w')
        tabla_numeros.heading(column="#0", text="Numeros Generados", anchor='w')
        numeros = sorted(generarNums(n))
        for i in range(n):
            numeros[i] = numExponencial(numeros[i], media)
            tabla_numeros.insert(parent='', index='end', values=str(numeros[i]))
        Pruebas_Bondad.calculo(n, numeros[0], numeros[-1], numeros, clases, 1 / media, False, False, 1, tabla,
                               resultadoBondad)
        graficar(n, numeros[0], numeros[-1], numeros, clases, "Exponencial")
    else:
        messagebox.showinfo("Info", "Ingrese una cantidad menor o igual a 50000")

def numExponencial(numero, media):
    exp = (-media * math.log(1 - numero))
    return exp

# Usamos algoritmo dado por el profesor y lo utilizamos las veces deseadas por el profesor
def poisson(lamd, n, tabla,tabla_numeros,resultadoBondad):
    tabla.delete(*tabla.get_children())
    tabla_numeros.delete(*tabla_numeros.get_children())
    if n <= 50000:
        tabla_numeros.column(column="#0", width=100, minwidth=50, anchor='w')
        tabla_numeros.heading(column="#0", text="Numeros Generados", anchor='w')
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
        for numero in z:
            tabla_numeros.insert(parent='', index='end', values=str(numero))
        Pruebas_Bondad.chi_poisson(n, z, lamd, tabla, resultadoBondad)
        graficar_poisson(n, z[0], z[-1], z, "Poisson")
    else:
        messagebox.showinfo("Info", "Ingrese una cantidad menor o igual a 50000")

# usamos el metodo box muller para obtener los numero, alternamos n1 y n2 segun si es par i o no
def normal(n, media, de, clases, tabla,tabla_numeros,resultadoBondad, metodo):
    tabla.delete(*tabla.get_children())
    tabla_numeros.delete(*tabla_numeros.get_children())
    if n <= 50000:
        if media <= 100:
            tabla_numeros.column(column="#0", width=100, minwidth=50, anchor='w')
            tabla_numeros.heading(column="#0", text="Numeros Generados", anchor='w')
            numeros_random = []
            if metodo == "1":
                if (n % 2) == 0:
                    for i in range(n // 2):
                        rnd1 = generarNums(1)
                        rnd2 = generarNums(1)
                        n1 = (pow(-2 * math.log(rnd1[0]), 1 / 2) * math.cos(2 * math.pi * rnd2[0])) * de + media
                        tabla_numeros.insert(parent='', index='end', values=str(n1))
                        n2 = (pow(-2 * math.log(rnd1[0]), 1 / 2) * math.sin(2 * math.pi * rnd2[0])) * de + media
                        numeros_random.append(n1)
                        numeros_random.append(n2)
                        tabla_numeros.insert(parent='', index='end', values=str(n2))
                else:
                    for i in range(n // 2):
                        rnd1 = generarNums(1)
                        rnd2 = generarNums(1)
                        n1 = (pow(-2 * math.log(rnd1[0]), 1 / 2) * math.cos(2 * math.pi * rnd2[0])) * de + media
                        tabla_numeros.insert(parent='', index='end', values=str(n1))
                        n2 = (pow(-2 * math.log(rnd1[0]), 1 / 2) * math.sin(2 * math.pi * rnd2[0])) * de + media
                        numeros_random.append(n1)
                        numeros_random.append(n2)
                        tabla_numeros.insert(parent='', index='end', values=str(n2))
                    rnd1 = generarNums(1)
                    rnd2 = generarNums(1)
                    n1 = (pow(-2 * math.log(rnd1[0]), 1 / 2) * math.cos(2 * math.pi * rnd2[0])) * de + media
                    tabla_numeros.insert(parent='', index='end', values=str(n1))
                    numeros_random.append(n1)

                numeros_random = sorted(numeros_random)
                # lo comentado es de testeo
                # cambiar = [1.56, 2.21, 3.15, 4.61, 4.18, 5.20, 4.87, 7.71, 5.15, 6.76, 7.28, 4.23, 3.54, 2.75, 4.69, 5.86, 6.25, 4.27, 4.91, 4.78, 2.46, 3.97, 6.09, 6.19, 4.20, 3.48, 5.83, 6.36, 5.90, 5.43, 3.87, 2.21, 3.74, 4.61, 4.18, 5.20, 4.28, 7.71, 5.15, 6.76, 7.28, 4.23, 3.21, 2.75, 4.69, 5.86, 6.25, 4.27, 4.91, 4.78]
                # cambiar.sort()
                # Intervalos.chicuad(n, cambiar[0], cambiar[-1], cambiar, clases, False, 4.7962, 1.4598279, 3, tabla)
                Pruebas_Bondad.calculo(n, numeros_random[0], numeros_random[-1], numeros_random, clases, False, media, de,
                                       3,
                                       tabla, resultadoBondad)
                graficar(n, numeros_random[0], numeros_random[-1], numeros_random, clases, "Normal")
            else:
                numeros_random = []
                for i in range(n):
                    numeros_a = generarNums(12)
                    res = (sum(numeros_a) - 6) * de + media
                    tabla_numeros.insert(parent='', index='end', values=str(res))
                    numeros_random.append(res)
                numeros_random = sorted(numeros_random)

                Pruebas_Bondad.calculo(n, numeros_random[0], numeros_random[-1], numeros_random, clases, False, media,
                                       de,
                                       3,
                                       tabla, resultadoBondad)
                graficar(n, numeros_random[0], numeros_random[-1], numeros_random, clases, "Normal")
        else:
            messagebox.showinfo("Info", "Ingrese una media menor o igual a 100")
    else:
        messagebox.showinfo("Infor", "Ingrese una cantidad menor o igual a 50000")

def generarNums(n):
    nums = []
    for i in range(n):
        num = random.random()
        nums.append(num)
    return nums

# calculos de probabilidad de cada distrib
def probNormal(marca, media, de, hasta,desde):
    res = ((math.exp((-0.5)*(pow(((marca-media)/de), 2))))/(de*math.sqrt(2*math.pi)))*(hasta-desde)
    return res

def probPoisson(lambd,numero): #(Lambda^D4*EXP(-Lambda))/FACT(D4)
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return ((pow(lambd,numero)*math.exp(-lambd))/factorial)

def probExponencial(lambd, marca, desde,hasta):
    res = (lambd*math.exp(-lambd*marca)) * (hasta - desde)
    return res

def probUniforme(n, clases):
    return round(1/clases)

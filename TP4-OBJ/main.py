import random
import distribuciones
from Eventos import eventos
from Servidores.cola import Cola
from Servidores.emplead import Empleado
from Servidores.empleado_recepcion import EmpleadoRecepcion
from Servidores.empleado_reparacion import EmpleadoReparacion
from Servidores.empleado_inspeccion import EmpleadoInspeccion
from Servidores.empleado_cobro import EmpleadoCobro
from Eventos import eventos
from Clientes.cliente import Cliente
from Clientes.aparato_electrodomestico import Aparato
from distribuciones import numExponencial
import tkinter as tk
from tkinter import ttk
import pandas as pd


if __name__ == '__main__':
    # Inicio temporizador
    vector_txt = ["evento", "reloj", "rnd_llegada_cliente", "tiempo_entre_llegada_cliente", "proxima_llegada_cliente",
                  "rnd_fin_recepcion", "tiempo_demora_recepcion", "fin_atencion_recepcion",
                  "rnd_reparacion", "tiempo_demora_reparacion", "fin_atencion_empleado_1", "fin_atencion_empleado_2",
                  "rnd_inspeccion", "tiempo_demora_inspeccion", "fin_atencion_inspeccion",
                  "rnd_fallos", "hay_fallas", " rnd_fin_atencion_cobro", "tiempo_demora_cobro", "fin_atencion_cobro",
                  "estado_recepcion",
                  "cola_recepcion", "estado1", "estado2", "cola_en_reparacion",
                  "estado_inspeccion", "cola_inspeccion", "estado_cobro", "cola_cobro", " contador_tres_fases",
                  "contador_atendidos",
                  "contador_volvieron_a_reparacion", "contador_demoraron_mas30_en_fase",
                  "ac_tiempo_demora_reparacion", "ac_tiempo_demora_de_los_que_no_esperaron"]
    # Definir la ruta y el nombre del archivo de Excel
    archivo_excel = 'datos.xlsx'

    # Crear un DataFrame vacío
    df = pd.DataFrame()
    df_temporal = pd.DataFrame([vector_txt])

    # Añadir la nueva fila al DataFrame principal
    df = pd.concat([df, df_temporal], ignore_index=True)



    # Parámetros para distribuciones
    media_llegada_clientes = 15
    media_atencion_recepcion = 3
    media_atencion_reparacion = 20
    media_atencion_inspeccion = 5
    media_atencion_cobro = 5

    # Cantidad de simulaciones
    num_sim = 500

    # Empleados (SERVIDORES)
    emp_recepcion = EmpleadoRecepcion("Libre", Cola(), media_atencion_recepcion)

    cola_reparacion = Cola()
    emp_reparacion_1 = EmpleadoReparacion("Libre", cola_reparacion, media_atencion_reparacion)
    emp_reparacion_2 = EmpleadoReparacion("Libre", cola_reparacion, media_atencion_reparacion)
    emp_reparacion_1.compañero = emp_reparacion_2
    emp_reparacion_2.compañero = emp_reparacion_1

    emp_inspeccion = EmpleadoInspeccion("Libre", Cola(), media_atencion_inspeccion)

    emp_cobro = EmpleadoCobro("Libre", Cola(), media_atencion_cobro)

    # Vector Estado
    evento = ""
    reloj = 0
    # Evento llegada_cliente
    tiempo_entre_llegada_cliente, rnd_llegada_cliente = numExponencial(media_llegada_clientes)
    proxima_llegada_cliente = tiempo_entre_llegada_cliente + reloj
    # Evento fin_atencion_recepcion
    rnd_fin_recepcion = tiempo_demora_recepcion = fin_atencion_recepcion = ""
    # Evento fin_atencion_reparacion
    rnd_reparacion = tiempo_demora_reparacion = fin_atencion_empleado_1 = fin_atencion_empleado_2 = ""
    # Evento fin_atencion_inspeccion
    rnd_inspeccion = tiempo_demora_inspeccion = fin_atencion_inspeccion = rnd_fallos = hay_fallas = ""
    # Evento fin_atencion_cobro
    rnd_fin_atencion_cobro = tiempo_demora_cobro = fin_atencion_cobro = ""
    # Empleado recepción
    estado_recepcion, cola_recepcion = emp_recepcion.mostrar_info()
    # Empleado Reparación
    estado1 = emp_reparacion_1.estado
    estado2 = emp_reparacion_2.estado
    cola_en_reparacion = len(cola_reparacion.cola)
    # Empleado Inspección
    estado_inspeccion, cola_inspeccion = emp_inspeccion.mostrar_info()
    # Empleado Cobro
    estado_cobro, cola_cobro = emp_cobro.mostrar_info()
    # Contadores
    contador_tres_fases = contador_atendidos = contador_volvieron_a_reparacion = contador_demoraron_mas30_en_fase = 0
    # Acumuladores
    ac_tiempo_demora_reparacion = ac_tiempo_demora_de_los_que_no_esperaron = 0

    vector = [evento, reloj, rnd_llegada_cliente, tiempo_entre_llegada_cliente, proxima_llegada_cliente,
              emp_recepcion.rnd, emp_recepcion.tiempo_demora, emp_recepcion.fin,
              emp_reparacion_1.rnd, emp_reparacion_1.tiempo_demora, emp_reparacion_1.fin, emp_reparacion_2.fin,
              emp_inspeccion.rnd, emp_inspeccion.tiempo_demora, emp_inspeccion.fin,
              emp_inspeccion.rnd_hay_fallos,emp_inspeccion.hay_fallos, emp_cobro.rnd, emp_cobro.tiempo_demora, emp_cobro.fin, emp_recepcion.estado,
              len(emp_recepcion.cola_empleado), emp_reparacion_1.estado, emp_reparacion_2.estado, len(emp_reparacion_1.cola_empleado),
              emp_inspeccion.estado, len(emp_inspeccion.cola_empleado), emp_cobro.estado, len(emp_cobro.cola_empleado), contador_tres_fases, contador_atendidos,
              contador_volvieron_a_reparacion, contador_demoraron_mas30_en_fase,
              ac_tiempo_demora_reparacion, ac_tiempo_demora_de_los_que_no_esperaron]
    vectort = vector

    # tabla.insert(parent='', index='end', values=vector)
    # Podría borrarse, se declara en cada iteración del FOR
    proximos = {'Llegada cliente': vector[4], 'Fin atención recepción': vector[7],
                'Fin atención reparación empleado 1': vector[10], 'Fin atención reparación empleado 2': vector[11],
                'Fin atención inspección': vector[14], 'Fin atención cobro': vector[19]}
    llaves = 'Llegada cliente', 'Fin atención recepción', 'Fin atención reparación empleado 1', 'Fin atención reparación empleado 2', 'Fin atención inspección', 'Fin atención cobro'
    indices = 4, 7, 10, 11, 14, 19
    df_temporal = pd.DataFrame([vector])
    # Añadir la nueva fila al DataFrame principal
    df = pd.concat([df, df_temporal], ignore_index=True)
    for i in range(num_sim):
        vector_ant = [evento, reloj, rnd_llegada_cliente, tiempo_entre_llegada_cliente, proxima_llegada_cliente,
              emp_recepcion.rnd, emp_recepcion.tiempo_demora, emp_recepcion.fin,
              emp_reparacion_1.rnd, emp_reparacion_1.tiempo_demora, emp_reparacion_1.fin, emp_reparacion_2.fin,
              emp_inspeccion.rnd, emp_inspeccion.tiempo_demora, emp_inspeccion.fin,
              emp_inspeccion.rnd_hay_fallos,emp_inspeccion.hay_fallos, emp_cobro.rnd, emp_cobro.tiempo_demora, emp_cobro.fin, emp_recepcion.estado,
              len(emp_recepcion.cola_empleado), emp_reparacion_1.estado, emp_reparacion_2.estado, len(emp_reparacion_1.cola_empleado),
              emp_inspeccion.estado, len(emp_inspeccion.cola_empleado), emp_cobro.estado, len(emp_cobro.cola_empleado), contador_tres_fases, contador_atendidos,
              contador_volvieron_a_reparacion, contador_demoraron_mas30_en_fase,
              ac_tiempo_demora_reparacion, ac_tiempo_demora_de_los_que_no_esperaron]
        proximos = {}
        for j in range(6):
            if str(vector[indices[j]]) != "":
                proximos[llaves[j]] = (float(vector[indices[j]]))

        minimo = min(proximos.values())
        for nombre, valor in proximos.items():

            if valor == minimo:
                reloj, evento = minimo, nombre
                break

        # Evento llegada_cliente
        if evento == 'Llegada cliente':
            tiempo_entre_llegada_cliente, rnd_llegada_cliente = numExponencial(media_llegada_clientes)
            proxima_llegada_cliente = tiempo_entre_llegada_cliente + reloj
            emp_recepcion.atender(Cliente(Aparato("", "", "", False), ""), reloj)

        # Evento fin_atencion_recepcion
        elif evento == 'Fin atención recepción':
            emp_recepcion.pasar_a(emp_reparacion_1, reloj)
            emp_recepcion.atender_siguiente(reloj)

        #Evento fin_atencion_reparacion_1
        elif evento == 'Fin atención reparación empleado 1':
            emp_reparacion_1.pasar_a(emp_inspeccion, reloj)
            emp_reparacion_1.atender_siguiente(reloj)

        elif evento == 'Fin atención reparación empleado 2':
            emp_reparacion_2.pasar_a(emp_inspeccion, reloj)
            emp_reparacion_2.atender_siguiente(reloj)

        # Evento fin_atencion_inspeccion
        elif evento == 'Fin atención inspección':
            emp_inspeccion.revisar(emp_cobro, emp_reparacion_1, reloj)
            emp_inspeccion.atender_siguiente(reloj)

        # Evento fin atencion cobro
        else:
        #elif evento == 'Fin atención cobro':
            emp_cobro.atender_siguiente(reloj)

        vector = [evento, reloj, rnd_llegada_cliente, tiempo_entre_llegada_cliente, proxima_llegada_cliente,
              emp_recepcion.rnd, emp_recepcion.tiempo_demora, emp_recepcion.fin,
              emp_reparacion_1.rnd, emp_reparacion_1.tiempo_demora, emp_reparacion_1.fin, emp_reparacion_2.fin,
              emp_inspeccion.rnd, emp_inspeccion.tiempo_demora, emp_inspeccion.fin,
              emp_inspeccion.rnd_hay_fallos,emp_inspeccion.hay_fallos, emp_cobro.rnd, emp_cobro.tiempo_demora, emp_cobro.fin, emp_recepcion.estado,
              len(emp_recepcion.cola_empleado), emp_reparacion_1.estado, emp_reparacion_2.estado, len(emp_reparacion_1.cola_empleado),
              emp_inspeccion.estado, len(emp_inspeccion.cola_empleado), emp_cobro.estado, len(emp_cobro.cola_empleado), contador_tres_fases, contador_atendidos,
              contador_volvieron_a_reparacion, contador_demoraron_mas30_en_fase,
              ac_tiempo_demora_reparacion, ac_tiempo_demora_de_los_que_no_esperaron]

        for n in range(len(vector)):
            if n in [2, 3,5,6,8,9,12,13,15,16,17,18]:
                if str(vector[n]) == str(vector_ant[n]):
                    vector[n] = ""

        if i < 500:
            df_temporal = pd.DataFrame([vector])
            # Añadir la nueva fila al DataFrame principal
            df = pd.concat([df, df_temporal], ignore_index=True)

    df.to_excel(archivo_excel, index=False)

    print("Filas añadidas exitosamente al archivo de Excel.")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random
from Servidores.cola import Cola
from Servidores.emplead import Empleado
from Servidores.empleado_reparacion import EmpleadoReparacion
from Clientes.cliente import Cliente
from Clientes.aparato_electrodomestico import Aparato
from distribuciones import numExponencial


def obtener_minimo(a, b, c, d, e, f):
    variables = locals()  # Obtener diccionario con los nombres y valores de las variables
    minimo = min(variables.values())  # Obtener el valor mínimo

    for nombre, valor in variables.items():
        if valor == minimo:
            return minimo, nombre


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Desde cuál hasta cuál mostrar

    # Parámetros para distribuciones
    media_llegada_clientes = 15
    media_atencion_recepcion = 3
    media_atencion_reparacion = 20
    mediap_atencion_inspeccion = 5
    media_atencion_cobro = 5

    # Cantidad de simulaciones
    num_sim = 100000

    # Empleados (SERVIDORES)
    emp_recepcion = Empleado("Libre",Cola())

    cola_reparacion = Cola()
    emp_reparacion_1 = EmpleadoReparacion("Libre", cola_reparacion)
    emp_reparacion_2 = EmpleadoReparacion("Libre", cola_reparacion)

    emp_inspeccion = Empleado("Libre",Cola())

    emp_cobro = Empleado("Libre", Cola())

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
    # Empleado Insprección
    estado_inspeccion, cola_inspeccion = emp_inspeccion.mostrar_info()
    # Empleado Cobro
    estado_cobro, cola_cobro = emp_cobro.mostrar_info()
    # Contadores
    contador_tres_fases = contador_atendidos = contador_volvieron_a_reparacion = contador_demoraron_mas30_en_fase = 0
    # Acumuladores
    ac_tiempo_demora_reparacion = ac_tiempo_demora_de_los_que_no_esperaron = 0

    vector = [evento, reloj, rnd_llegada_cliente, tiempo_entre_llegada_cliente, proxima_llegada_cliente, rnd_fin_recepcion, tiempo_demora_recepcion, fin_atencion_recepcion,
              rnd_reparacion, tiempo_demora_reparacion, fin_atencion_empleado_1, fin_atencion_empleado_2, rnd_inspeccion, tiempo_demora_inspeccion, fin_atencion_inspeccion,
              rnd_fallos, hay_fallas, rnd_fin_atencion_cobro, tiempo_demora_cobro, fin_atencion_cobro, estado_recepcion, cola_recepcion, estado1, estado2, cola_en_reparacion,
              estado_inspeccion, cola_inspeccion, estado_cobro, cola_cobro, contador_tres_fases, contador_atendidos, contador_volvieron_a_reparacion, contador_demoraron_mas30_en_fase,
              ac_tiempo_demora_reparacion, ac_tiempo_demora_de_los_que_no_esperaron]

    proximos = {'Llegada cliente': vector[4], 'Fin atención recepción': vector[7], 'Fin atención reparación empleado 1': vector[10], 'Fin atención reparación empleado 2': vector[11], 'Fin atención inspección': vector[14], 'Fin atención cobro': vector[19]}
    llaves = 'Llegada cliente', 'Fin atención recepción', 'Fin atención reparación empleado 1', 'Fin atención reparación empleado 2', 'Fin atención inspección','Fin atención cobro'
    indices = 4, 7, 10, 11, 14, 19
    for i in range(num_sim):
        proximos = {}
        for j in range(5):
            if str(vector[indices[j]]) != "":
                proximos[llaves[j]] = (float(vector[indices[j]]))

        minimo = min(proximos.values())
        for nombre, valor in proximos.items():
            if valor == minimo:
                reloj, evento = minimo, nombre
                break

        # Evento llegada_cliente
        if evento == 'Llegada cliente':
            # Calcula la próxima llegada
            tiempo_entre_llegada_cliente, rnd_llegada_cliente = numExponencial(media_llegada_clientes)
            proxima_llegada_cliente = tiempo_entre_llegada_cliente + reloj
            if emp_recepcion.es_libre():
                aparato = Aparato("Siendo Atendido", reloj, 0, False)
                cliente = Cliente(aparato, "Siendo Atendido")
                emp_recepcion.ocupar(cliente)
                estado_recepcion = emp_recepcion.estado
                tiempo_demora_recepcion, rnd_fin_recepcion = numExponencial(media_atencion_recepcion)
                fin_atencion_recepcion = reloj + tiempo_demora_recepcion

            else:
                aparato = Aparato("Esperando Recepcion", 0, 0, True)
                cliente = Cliente(aparato, "Esperando recepcion")
                emp_recepcion.cola_empleado.agregar(cliente)
                cola_recepcion = len(emp_recepcion.cola_empleado)

        # Evento fin_atencion_recepcion
        elif evento == 'Fin atención recepción':
            tiempo_demora_reparacion, rnd_reparacion = numExponencial(media_atencion_reparacion)
            if emp_reparacion_1.es_libre() and emp_reparacion_2.es_libre():
                tiempo_demora_reparacion *= 0.5
                fin_atencion_empleado_1 = tiempo_demora_reparacion + reloj
                emp_reparacion_1.ocupar(emp_recepcion.atendiendo_a)
                emp_reparacion_2.ayudar()
                emp_reparacion_1.atendiendo_a.estado = "Esperando aparato"
                emp_reparacion_1.atendiendo_a.aparato_electrodomestico.iniciar_reparacion(reloj)

            elif emp_reparacion_1.esta_ayudando():
                fin_atencion_empleado_2 = (fin_atencion_empleado_2 - reloj) / 0.5 + reloj
                fin_atencion_empleado_1 = tiempo_demora_reparacion + reloj
                emp_reparacion_1.ocupar(emp_recepcion.atendiendo_a)
                emp_reparacion_1.atendiendo_a.estado = "Esperando aparato"
                emp_reparacion_1.atendiendo_a.aparato_electrodomestico.iniciar_reparacion(reloj)

            elif emp_reparacion_2.esta_ayudando():
                fin_atencion_empleado_1 = (fin_atencion_empleado_1 - reloj)/0.5 + reloj
                fin_atencion_empleado_2 = tiempo_demora_reparacion + reloj
                emp_reparacion_2.ocupar(emp_recepcion.atendiendo_a)
                emp_reparacion_2.atendiendo_a.estado = "Esperando aparato"
                emp_reparacion_2.atendiendo_a.aparato_electrodomestico.iniciar_reparacion(reloj)
            else:
                tiempo_demora_reparacion = rnd_reparacion = ""

            if len(emp_recepcion.cola_empleado) > 0:
                emp_recepcion.atendiendo_a = emp_recepcion.cola_empleado.sacar()
                tiempo_demora_recepcion, rnd_fin_recepcion = numExponencial(media_atencion_recepcion)
                fin_atencion_recepcion = reloj + tiempo_demora_recepcion
            else:
                emp_recepcion.desocupar()
                fin_atencion_recepcion = rnd_fin_recepcion = tiempo_demora_recepcion = ""
            cola_recepcion = len(emp_recepcion.cola_empleado)

        # Evento fin_atencion_reparacion_1
        elif evento == 'Fin atención reparación empleado 1':
            if emp_reparacion_2.esta_ayudando():
                emp_reparacion_2.estado = "Libre"
            if emp_inspeccion.es_libre():
                emp_inspeccion.ocupar(emp_reparacion_1.atendiendo_a)
                emp_inspeccion.atendiendo_a.aparato_electrodomestico.estado = "Siendo Inspeccionado"
            else:
                emp_inspeccion.cola_empleado.agregar(emp_reparacion_1.atendiendo_a)
                emp_inspeccion.atendiendo_a.aparato_electrodomestico.estado = "Esperando Inspeccion"
            emp_reparacion_1.desocupar()
            if len(cola_reparacion.cola) > 0:
                tiempo_demora_reparacion, rnd_reparacion = numExponencial(media_atencion_reparacion)
                if not emp_reparacion_2.es_ocupado():
                    tiempo_demora_reparacion *= 0.5
                    emp_reparacion_2.ayudar()
                fin_atencion_empleado_1 = reloj + tiempo_demora_recepcion
                emp_reparacion_1.ocupar(cola_reparacion.cola.sacar())
            elif emp_reparacion_2.es_ocupado():
                fin_atencion_empleado_2 = (fin_atencion_empleado_2 - reloj) * 0.5 + reloj
                emp_reparacion_1.ayudar()
            if len(cola_reparacion.cola) == 0:
                tiempo_demora_reparacion = rnd_reparacion = fin_atencion_empleado_1 = ""

                # Evento fin_atencion_reparacion_2
        elif evento == 'Fin atención reparación empleado 2':
            if emp_reparacion_1.esta_ayudando():
                emp_reparacion_1.estado = "Libre"   # esto faltaba
            if emp_inspeccion.es_libre():
                emp_inspeccion.ocupar(emp_reparacion_2.atendiendo_a)
                emp_inspeccion.atendiendo_a.aparato_electrodomestico.estado = "Siendo Inspeccionado"

            else:
                emp_inspeccion.cola_empleado.agregar(emp_reparacion_2.atendiendo_a)
                emp_inspeccion.atendiendo_a.aparato_electrodomestico.estado = "Esperando Inspeccion"
            emp_reparacion_2.desocupar()
            if len(cola_reparacion.cola) > 0:
                tiempo_demora_reparacion, rnd_reparacion = numExponencial(media_atencion_reparacion)
                if not emp_reparacion_1.es_ocupado():
                    tiempo_demora_reparacion *= 0.5
                    emp_reparacion_1.ayudar()
                fin_atencion_empleado_2 = reloj + tiempo_demora_recepcion
                emp_reparacion_2.ocupar(cola_reparacion.cola.sacar())
            elif emp_reparacion_1.es_ocupado():
                fin_atencion_empleado_1 = (fin_atencion_empleado_1 - reloj) * 0.5 + reloj
                emp_reparacion_2.ayudar()
            if len(cola_reparacion.cola) == 0:
                tiempo_demora_reparacion = rnd_reparacion = fin_atencion_empleado_2 = ""

        # Evento fin_atencion_inspeccion
        elif evento == 'Fin atención inspección':
            if random.random() <= 0.2:
                cola_reparacion.agregar(emp_inspeccion.atendiendo_a)
                emp_inspeccion.atendiendo_a.aparato_electrodomestico.iniciar_reparacion(emp_inspeccion.atendiendo_a.aparato_electrodomestico.iniciar_reparacion)
                emp_inspeccion.desocupar()
            elif emp_cobro.es_libre():
                emp_cobro.ocupar(emp_inspeccion.atendiendo_a)
                emp_cobro.estado = "Siendo Cobrado"

            else:
                emp_cobro.cola_empleado.agregar(emp_reparacion_2.atendiendo_a)
                emp_cobro.estado = "Esperando Cobro"
            emp_inspeccion.desocupar()

        # Evento fin atencion cobro
        elif evento == 'Fin atención cobro':
            pass

        vector = [evento, reloj, rnd_llegada_cliente, tiempo_entre_llegada_cliente, proxima_llegada_cliente,
                  rnd_fin_recepcion, tiempo_demora_recepcion, fin_atencion_recepcion,
                  rnd_reparacion, tiempo_demora_reparacion, fin_atencion_empleado_1, fin_atencion_empleado_2,
                  rnd_inspeccion, tiempo_demora_inspeccion, fin_atencion_inspeccion,
                  rnd_fallos, hay_fallas, rnd_fin_atencion_cobro, tiempo_demora_cobro, fin_atencion_cobro, estado_recepcion,
                  cola_recepcion, estado1, estado2, cola_en_reparacion,
                  estado_inspeccion, cola_inspeccion, estado_cobro, cola_cobro, contador_tres_fases, contador_atendidos,
                  contador_volvieron_a_reparacion, contador_demoraron_mas30_en_fase,
                  ac_tiempo_demora_reparacion, ac_tiempo_demora_de_los_que_no_esperaron]
        if i < 500:
            print(vector)



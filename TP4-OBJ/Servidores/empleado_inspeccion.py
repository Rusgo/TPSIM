from Servidores.emplead import Empleado
import random


class EmpleadoInspeccion(Empleado):
    def __init__(self, estado, cola, media):
        super().__init__(estado, cola, media)
        self.hay_fallos = False
        self.rnd_hay_fallos = ""

    def ocupar(self, cliente, reloj):
        super().ocupar(cliente, reloj)
        cliente.aparato_electrodomestico.estado ="Siendo Inspeccionado"

    def esperar(self, cliente):
        cliente.aparato_electrodomestico.estado = "Esperando Inspeccion"

    def revisar(self, empleado_siguiente, empleado_anterior, reloj):
        self.rnd_hay_fallos = random.random()
        self.hay_fallos = False
        if self.rnd_hay_fallos < 0.25:
            self.hay_fallos = True
            self.pasar_a(empleado_anterior, reloj)
        else:
            self.pasar_a(empleado_siguiente, reloj)

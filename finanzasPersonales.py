from Ingresos import Ingreso
from Egresos import Egreso

ingreso = Ingreso()
egreso = Egreso()


class FinanzasP:
    def __init__(self, id, monto):
        self.id = id
        self.nombre = nombre
        self.monto = monto

    def montoFinal(self):
        listaIngresos = ingresos.ingresosTotales()
        listaEgresos = egresos.egresostotales()
        totalIngresos = 0.00
        totalEgresos = 0.00

        for ingreso in listaIngresos:
            totalIngresos = totalIngresos + ingreso[1]

        for egreso in listaEgresos:
            totalEgresos = totalEgresos + egreso[1]

        montoFinalCuenta = self.monto + totalIngresos - totalEgresos

        return montoFinalCuenta

    def ingresoNew(self, id, monto):
        ingresos.ingresoNew(id, monto)

    def egresoNew(self, id, monto):
        egresos.egresoNew(id, monto)

    def registroIngresos(self):
        ingresos.showIngresos()

    def registroEgresos(self):
        egresos.showEgresos()

    def registrosTransacciones(self):
        ingresos.showIngresos()
        egresos.showEgresos()

    def obtenerNombre(self):
        return self.nombre

    def obtenerId(self):
        return self.id
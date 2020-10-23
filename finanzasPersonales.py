from Ingresos import Ingreso
from Egresos import Egreso

ingreso = Ingreso()
egreso = Egreso()


class FinanzasP:
    def __init__(self, id, monto):
        self.id = id
        self.monto = monto

    def registroIngreso(self, id, monto):
        ingreso.ingresoNew(id, monto)

    def registroEgreso(self, id, monto):
        egreso.egresoNew(id, monto)

    def totalMonto(self):
        ingresos = ingreso.totalIngreso()
        egresos = egreso.totalEgresos()
        totalMonto = float(ingresos - egresos)
        return totalMonto

    def mostrarIngresos(self):
        ingreso.showIngreso()

    def mostrarEgresos(self):
        ingreso.showEgresos()

    def mostrarTransacciones(self):
        ingreso.showIngreso()
        egreso.showEgresos()

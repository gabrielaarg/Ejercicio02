class Egreso:
    def __init__(self):
        self.listaEgresos = []

    def egresoNew(self, id, monto):
        egresoNew = (id, monto)
        self.listaEgresos.append(egresoNew)
        return self.listaEgresos

    def showEgresos(self):
        for egreso in self.listaEgresos:
            print(f"Id: {egreso[0]} Monto: {egreso[1]}")

    def egresosTotales(self):
        total = 0
        for egreso in self.listaEgresos:
            total += float(egreso[1])
        return total

class Ingreso:
    def __init__(self):
        self.listaIngresos = []

    def ingresoNew(self, id, monto):
        newingreso = (id, monto)
        self.listaIngresos.append(newingreso)
        return self.listaIngresos

    def showIngreso(self):
        for ingreso in self.listaIngresos:
            print(f"Id: {Ingreso[0]} Monto: {ingreso[1]}")

    def ingresosTotales(self):
        total = 0
        for ingreso in self.listaIngresos:
            total += float(ingreso[1])
        return total

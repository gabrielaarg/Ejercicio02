from finanzasPersonales import FinanzasP

while True:
    print("Instrucciones:")
    print("0  ->Salir")
    print("1  ->Iniciar cuenta a $0.00")
    print("2  ->Registrar Ingreso o Egreso")
    print("3  ->Registro de Ingresos")
    print("4  ->Registro de Egresos")
    print("5  ->Registro de transacciones")
    print("6  ->Total en cuenta")
    option = input("Ingrese una opción: ")

    if option == "0":
        break
    elif option == "1":
        id = input("Ingrese el Id de su cuenta: ")
        nombre = input("Ingrese su nombre: ")
        monto = 0.00
        finanza = FinanzasP
        (id, nombre, monto)
        print("Se ha inicializado su cuenta a $0.00")
    elif option == "2":
        option1 = input(
            "1. Registrar Ingreso. 2. Registrar Egreso. Ingrese una opción: "
        )

ingreso = True
while True:
    print("--MENU--")
    print("1. Pago tarjeta de Credito")
    print("2. Simulacion de compras")
    print("3. Salir")

    op = int(input("Ingrese su opcion: "))

    if op == 1:
        print("Pagando..")
    elif op == 2:
        print("Comprando..")
    elif op == 3:
        print("Saliendo..")
        #break
        ingreso = False
    else:
        print("Opcion no valida")
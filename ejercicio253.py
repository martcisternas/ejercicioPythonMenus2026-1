ingreso = True
saldo = 400000
deuda = 100000
TotalCompra = 0
cont = 0
while True:
    print("--MENU--")
    print("1. Pago tarjeta de Credito")
    print("2. Simulacion de compras")
    print("3. Salir")
    while True:
        try:
            op = int(input("Ingrese su opcion: "))
            break
        except ValueError:
            print("Ingrese un valor numerico del 1 al 3")

    if op == 1:
        print("Pagando..")
        print("La deuda es de $",deuda)
        montoPagar = int(input("Ingrese monto a pagar: "))
        if montoPagar >= 0:
            if montoPagar <= deuda:
                deuda = deuda - montoPagar
                saldo = saldo + montoPagar
            print("Pago exitoso!, El saldo de la deuda es: $",deuda)
        else:
            print("El monto excede la deuda.")
    elif op == 2:
       print("Comprando...")
       print("Su saldo para comprar es $",saldo)
       for i in range(saldo):
           
           cont = cont + 1

           print(f"Compra {cont}")
           while True:
                try:
                    montoCompra = int(input("Ingrese monto de la compra: $"))
                    break
                except ValueError:
                    print("Error!, Ingrese un monto valido!!, Ingrese nuevamente:")
            
            
           if montoCompra >= 0 :
               if saldo < montoCompra:
                    saldo = saldo - montoCompra
                    deuda = deuda + montoCompra
                    print("Su nuevo saldo es: $",saldo)
                    if montoCompra == 0 or saldo <= 0:
                        break
               else:
                   print("El saldo es insuficiente")
                   break
                   
           else:
               print("Porfavor ingrese un numero mayor a cero")
               cont = cont + 1
               print(f"compra {cont}")


    elif op == 3:
        print("Saliendo..")
        #break
        ingreso = False
        
    else:
        print("Opcion no valida")
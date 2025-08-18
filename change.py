def change():
    expense = 23.75
    money = 100
    print("ingresar gasto:")
    print(expense)
    print("dinero recibido")
    print(money)
    print("")
    print("vuelto")
    print("")
    print("pesos:")
    vuelto = money - expense
    pesos = int(vuelto)
    print(pesos)
    print("centavos:")
    centavos = int((vuelto - pesos)*100)
    print(centavos)
change()

    

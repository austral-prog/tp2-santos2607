def change():
    expense = 23.75
    money = 100
     vuelto = money-expense
    centavos = (vuelto-int(vuelto))*100 

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    vuelto = money - expense
    pesos = int(vuelto)
    print(pesos)
    print("Centavos:")
    centavos = int((vuelto - pesos)*100)
    print(centavos)
change()

   
    

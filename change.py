def change():
    expense = 23.75
    money = 100
    vuelto = money-expense
    centavos = (vuelto-int(vuelto))*100 

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(str(money) + "\n")

    print("Vuelto" +"\n")

    print("Pesos")
    print(int(vuelto))
    print("Centavos:")
    print(int(centavos))

change()

    

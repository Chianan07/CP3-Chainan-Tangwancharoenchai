usernameInput = input("username : ")
passwordInput = input("password : ")
if usernameInput == "champ" and passwordInput == "123456":
    print("----KARUMA SHOP----")
    print("1. Apple  x 1 : 30")
    print("2. Banana x 1 : 15")
    userSelected = int(input("Choose Number that you want to buy(if you want to buy 1 and 2 please use number3) : "))
    if userSelected == 1:
        price = 30
        amount = int(input("How many pieces do you want : "))
        result = price * amount
        print("Total : ", result)
    elif userSelected == 2:
        price = 15
        amount = int(input("How many pieces do you want : "))
        result = price * amount
        print("Total : ", result)
    elif userSelected == 3:
        price1 = 30
        price2 = 15
        amount1 = int(input("How many pieces of apple do you want  : "))
        amount2 = int(input("How many pieces of banana do you want : "))
        result = (price1 * amount1) + (price2 * amount2)
        print("Total : ", result)
        print("----Thank you----")
    else:
        print("Error! Please Select 1 or 2 or 3")
else:
    print("Username or password Incorrect.")              

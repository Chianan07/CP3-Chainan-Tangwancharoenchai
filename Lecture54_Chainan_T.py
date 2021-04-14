def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "123456":
        return showMenu()
    else:
        print("Please try again!!!")
        return login()
def showMenu():
    print("---- KARUMA SHOP ----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input("Choose number 1 or 2 : "))
    if userSelected == 1:
        return vatCalculation(int(input("Total Price : ")))
    elif userSelected == 2:
        return priceCalculation()
    else:
        print("Try Again!!!")
        return menuSelect()
def vatCalculation(totalprice):
    vat = 7
    result = int(totalprice) + (int(totalprice) * vat / 100)
    return result
def priceCalculation():
    price1 = int(input("First Production Price : "))
    price2 = int(input("Second Production Price : "))
    return vatCalculation(price1 + price2)

print("----Welcome----")
print(login())
print("----Thank you----")

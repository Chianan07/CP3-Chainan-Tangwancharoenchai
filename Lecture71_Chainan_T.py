menuList = []
priceList = []
def showBill():
    print("KARUMA SHOP".center(21, "-"))
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        
while True:
    menuName = input("Please enter Menu : ")
    if(menuName.lower() == "exit"):  
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
        
print(menuList, priceList)
showBill()
print("")
print("Total Price :", sum(priceList))

inventory = {"twix": 1.00, 
            "kitkat": 1.00, 
            "coke": 1.50, 
            "water": 1.00,
            "reeses": 1.50
            }

def machine():
    cart = {}
    total = 0
    print("-----Vending Machine-----")
    print("Welcome! Here is out inventory:")
    print("\nINVENTORY\n------------")
    for item in inventory:
            print(str(item).upper() + ": " + str(inventory[item]))
    budgetValid = False
    while budgetValid == False:
        budget = input("\nHow much money do you have? ")
        if budget.isnumeric() == True:
            budgetValid = True
        else:
            print("Enter an integer")


    buyAgain = True
    while buyAgain == True:
        wrongPurchase = True
        while wrongPurchase == True:
            purchase = input("What would you like to purchase? ")

            if purchase not in inventory:
                print("That is not in our inventory")
            
            else:
                wrongPurchase = False

        tooMuch = True
        while tooMuch == True:
            purchaseQuantity = int(input("How much? "))
            price = (float(inventory[purchase]) * float(purchaseQuantity))
            cart[purchase] = (purchaseQuantity)
            total += float(price)
            if (float(budget) - float(price)) < 0:
                print("\nCOST: " + str(price) + " CASH: " + str(budget))
                print("\nYou don't have enough money for that amount\n") 
            else:
                budget = float(budget)
                budget -= float(price)
                tooMuch = False

        print("\nTOTAL COST: " + str(total) + " CASH: " + str(budget))
        print("\nCART: ")
        for item in cart:
            print(item + ": " + str(cart[item]).upper())

        choice = input("\nWould you like to purchase another item?\n")
        if choice == "yes":
            pass
        else:
            buyAgain = False


machine()

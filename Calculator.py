def calculator():
    print("*****CALCULATOR*****")
    active = True

    while active == True:
        firstNum = int(input("Please enter the first number: "))
        secNum = int(input("Please enter the second number: "))
        operator = input("Please enter an operator(+, -, *, /): ")

        if operator == "+":
            result = (int(firstNum) + int(secNum)) 
            print("")
            print(str(firstNum) + " + " + str(secNum) + " equals " + str(result))
        elif operator == "-":
            result = (int(firstNum) - int(secNum))  
            print("")
            print(str(firstNum) + " - " + str(secNum) + " equals " + str(result))
        elif operator == "*":
            result = (int(firstNum) * int(secNum))  
            print("")
            print(str(firstNum) + " * " + str(secNum) + " equals " + str(result))
        elif operator == "/":
            result = (int(firstNum) / int(secNum)) 
            print("")
            print(str(firstNum) + " / " + str(secNum) + " equals " + str(result))

        print("")
        choice = input("would you like to use the calculator again? (yes/no): ")

        if choice == "yes":
            pass
        elif choice == "no":
            print("")
            print("Thanks for using the calculator")
            active = False
calculator()

def intro():
    print("*****TEMPERATURE CONVERTOR*****")
    print("")

def inputs():
    temp = input("Input the temperature you would like to convert: ")
    units = ["fahrenheit", "celsius", "kelvin"]
    print("")

    print("----UNITS----")
    for unit in units:
        print("- " + unit.upper() + "\n")
    validationBeg = False
    validationEnd = False

    while validationBeg == False:
        begUnit = input("What is the starting unit type?: ").lower()
        if begUnit in units:
            validationBeg == True
            break
        else:
            print("Enter a valid unit")
        
    while validationBeg == False:
        endUnit = input("What is the ending unit type?: ").lower()
        if endUnit in units:
            validationBeg == True
            break
        else:
            print("Enter a valid unit")

    if begUnit == "fahrenheit" and endUnit == "celsius":
        newT = FtoC(temp)
        print(str(temp) + " " + begUnit + " is " + str(newT) + " " + endUnit)

    if begUnit == "fahrenheit" and endUnit == "kelvin":
        newT = FtoK(temp)
        print(str(temp) + " " + begUnit + " is " + str(newT) + " " + endUnit)

    if begUnit == "celsius" and endUnit == "fahrenheit":
        newT = CtoF(temp)
        print(str(temp) + " " + begUnit + " is " + str(newT) + " " + endUnit)

    if begUnit == "celsius" and endUnit == "kelvin":
        newT = CtoK(temp)
        print(str(temp) + " " + begUnit + " is " + str(newT) + " " + endUnit)

    if begUnit == "kelvin" and endUnit == "fahrenheit":
        newT = KtoF(temp)
        print(str(temp) + " " + begUnit + " is " + str(newT) + " " + endUnit)

    if begUnit == "kelvin" and endUnit == "celsius":
        newT = KtoC(temp)
        print(str(temp) + " " + begUnit + " is " + str(newT) + " " + endUnit)


def FtoC(temp):
    newTemp = (int(temp) - 32) * (5/9)
    return newTemp

def FtoK(temp):
    newTemp = (int(temp) - 32) * (5/9) + 273.15
    return newTemp

def CtoF(temp):
    newTemp = (int(temp) + (9/5)) + 32
    return newTemp

def CtoK(temp):
    newTemp = int(temp) + 273.15
    return newTemp

def KtoF(temp):
    newTemp = (int(temp) - 273.15) + (9/5) + 32
    return newTemp

def KtoC(temp):
    newTemp = (int(temp) - 273.15)
    return newTemp



intro()

active = True

while active == True:
    inputs()
    active2 = True

    while active2 == True:
        choice = input("\n Would you like to convert another temperature? (yes/no): ")

        if choice == "yes":
            active2 = False
            
        elif choice == "no":
            print("\n Goodbye")
            active = False
            active2 = False

        else:
            print("That is not an option")

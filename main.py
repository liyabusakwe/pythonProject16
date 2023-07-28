import math
import re
import sys


def containsNumber(word:str):
    return any(char.isdigit() for char in word)

def continueCalc():
    valid = False
    while valid == False:
        print("Enter \"con\" to continue")
        option = str(input()).strip()
        if option and option.upper() == "CON":
            valid = True
        else:
            print("***Please enter the correct option please***")

def optionAfterCalc(op:str):
    print("****************************************************************************")
    print(" 1. Calculate "+op+" again")
    print(" 2. Go to main menu")
    print("****************************************************************************")

    option = ""
    valid = False
    while valid == False:
        print("Enter "+op+" or Main to choose option")
        option = str(input()).strip()
        if option and option.upper() in [op.upper(), "MAIN"]:
            valid = True
        else:
            print("***Please enter the correct option please***")

    if option.upper() == "INVESTMENT":
        investment()
    elif option.upper() == "BOND":
        bond()
    else:
        mainMenu()

def term(c:str):
    if c == "Investment":
        valid = False
        o = ""
        while valid == False:
            print("Enter the number of years for the investment: ")
            o = str(input()).strip()
            if o and o.isnumeric():
                valid = True
            else:
                print("Invalid Input!")
        return o
    else:
        valid = False
        o = ""
        while valid == False:
            print("Enter the number of months to pay the the bond: ")
            o = str(input()).strip()
            if o and o.isnumeric():
                valid = True
            else:
                print("Invalid Input!")
        return o

def interest():
    valid = False
    a = ""
    while valid == False:
        print("Enter number of the interest (%): ")
        a = str(input()).strip()
        if re.match("^[0-9]+\.{1}[0-9]+$", a) or re.match("^[0-9]+$", a):
            valid = True
        else:
            print("invalid Input!")
    r = float(a)/100
    return str(r)

def amount():
    valid = False
    a = ""
    while valid == False:
        print("Enter amount of money of the present value: ")
        a = str(input()).strip()
        if re.match("^[0-9]+\.{1}[0-9]+$", a) or re.match("^[0-9]+$", a):
            valid = True
        else:
            print("invalid Input!")
    return a

def typeInterest():
    valid = False
    o = ""
    while valid == False:
        print("Enter the type of interest of investment(Simple or Compound):")
        o = str(input()).strip()
        if o and not containsNumber(o) and o.upper() == "SIMPLE":
            valid = True
        elif o and not containsNumber(o) and o.upper() == "COMPOUND":
            valid = True
        else:
            print("Invalid Input!")
    return o

def compoundCalc(p: str, r: str, t: str):
    return float(p)*math.pow((1+float(r)),float(t))
def simpleCalc(p:str, r:str, t:str):
    return float(p)*(1+(float(r) * float(t)))
def bondCalc(p:str, i:str, n:str):
    return (float(i)*float(p))/(1-math.pow((1+float(i)),(-1*float(n))))
def bond():
    print("============================================================================")
    print("----------------------------ZETA Bond-Calculator----------------------------")
    print("****************************************************************************")
    p = amount()
    r = interest()
    t = term("Bond")
    x = bondCalc(p,str(float(r)/12),t)
    print("============================================================================")
    print("Price Of Property\t\t\t\t\t: R" + "{:.2f}".format(float(p)))
    print("Interest Percentage\t\t\t\t\t: " + str(round(float(r) * 100, 2)) + "%")
    print("Months of Payment\t\t\t\t\t: " + t)
    print("")
    print("Payments per Month\t\t\t\t\t: R" + "{:.2f}".format(round(x, 2)))
    print("============================================================================")

    continueCalc()
    optionAfterCalc("Bond")

def investment():
    print("============================================================================")
    print("-------------------------ZETA Investment-Calculator-------------------------")
    print("****************************************************************************")
    p = amount()
    r = interest()
    t = term("Investment")
    i = typeInterest()
    if i.upper() == "SIMPLE":
        a = simpleCalc(p,r,t)
    else:
        a = compoundCalc(p, r, t)
    print("============================================================================")
    print("Amount Invested\t\t\t\t\t\t: R"+"{:.2f}".format(float(p)))
    print("Interest Percentage\t\t\t\t\t: "+str(round(float(r)*100, 2))+"%")
    print("Years of Investment\t\t\t\t\t: "+t)
    print("Type of Interest\t\t\t\t\t: " + i.upper())
    print("")
    print("Total Amount after end of investment: R" + str(round(a, 2)))
    print("============================================================================")

    continueCalc()
    optionAfterCalc("Investment")

def mainMenu():
    print("============================================================================")
    print("--------------------------ZETA Finance Calculator---------------------------")
    print("****************************************************************************")
    print(" 1. Investment \t-To Calculate the amount of interest you'll earn on interest")
    print(" 2. Bond\t\t-To Calculate the amount you'll have to pay on a home loan")
    print("")
    print(" 3. Exit Calculator")
    print("============================================================================")
    valid = False
    o = ""
    while valid == False:
        print("Enter the name of the option(Investment or Bond or Exit):")
        o = str(input()).strip()
        if o and not containsNumber(o) and o.upper() == "INVESTMENT":
            valid = True
        elif o and not containsNumber(o) and o.upper() == "BOND":
            valid = True
        elif o and not containsNumber(o) and o.upper() == "EXIT":
            valid = True
        else:
            print("Invalid Input!")
    if o.upper() == "INVESTMENT":
        investment()
    if o.upper() == "BOND":
        bond()
    if o.upper() == "EXIT":
        print("----------------------------------GOODBYE-----------------------------------")
        sys.exit()

mainMenu()
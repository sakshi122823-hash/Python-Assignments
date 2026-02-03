#check wheather number is positive negative or zero 

def Checknum(No):
    if No == 0:
        print("Zero")
    elif No > 0:
        print("Positive")
    else:
        print("Negative")

number = int(input("enter the number : "))

Checknum(number)
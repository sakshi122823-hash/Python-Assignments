def divisible(No):
    if No % 3 == 0 and  No % 5 == 0:
        print("the number is divisible by 3 and 5")
    else:
        print("the number is not divisible by 3 and 5")


num = int(input("enter the number "))
divisible(num)

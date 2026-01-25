no1 = int(input("Enter a number: "))
no2 = int(input("Enter a number: "))

minimumnum = lambda x,y : x if x < y else y
print(minimumnum(no1,no2))
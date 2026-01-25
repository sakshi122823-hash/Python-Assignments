no1 = int(input("Enter a number: "))
no2 = int(input("Enter a number: "))

grater = lambda x,y : x if x > y else y
print(grater(no1,no2))
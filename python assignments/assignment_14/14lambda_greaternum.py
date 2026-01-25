no1 = int(input("Enter a number: "))
no2 = int(input("Enter a number: "))
no3=int(input("Enter a number: "))
graeternum = lambda x,y,z : x if x > y and x > z  else (y if y > z else z)
print(graeternum(no1,no2,no3))



# method 2 
greaternum = lambda x, y, z: max(x, y, z)

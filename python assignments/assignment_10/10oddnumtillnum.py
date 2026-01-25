def evennumber(num):
    for i in range(1,num+1):
        if i % 2 != 0 :
            print(i)

    
number = int(input("enter number: "))
evennumber(number)

def sumnatural(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum + i
    print("the sum of n natural number is :",sum)
        


number = int(input("give number :"))

sumnatural(number)
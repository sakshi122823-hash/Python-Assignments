def pattern(n):
    for i in range( n , 0 ,- 1):
        print("* " * i)




number = int(input("enter number :"))

if __name__=="__main__":
    pattern(number)
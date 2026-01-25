def reverse(n):
    for i in range(n ,0,-1):
        print(i,end="  ")

number = int(input("enter number : "))
if __name__=="__main__":
    reverse(number)

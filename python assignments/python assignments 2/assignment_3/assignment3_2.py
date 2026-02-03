def maxnum_list():
    n = int(input("enter the number of elements : "))
    numbers = []
    
    for i in range(n):
        
        num = int(input("enter the elements : "))
        numbers.append(num)
    print("maximum number from list is  : ",max(numbers))




if __name__=="__main__":
    maxnum_list()
def minnum_list():
    n = int(input("enter the number of elements : "))
    numbers = []
    
    for i in range(n):
        
        num = int(input("enter the elements : "))
        numbers.append(num)
    print("maximum number from list is  : ",min(numbers))




if __name__=="__main__":
    minnum_list()


    
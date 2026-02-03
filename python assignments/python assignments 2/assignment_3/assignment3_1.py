def add_listelememnts():
    n = int(input("enter the number of elements : "))
    numbers = []
    
    for i in range(n):
        
        num = int(input("enter the elements : "))
        numbers.append(num)
    print("addition of elements in the list is : ",sum(numbers))




if __name__=="__main__":
    add_listelememnts()
def pattern(n):
    for i in range(n):
        for j in range(1,n+1):
            print(j , end=" ")
        
        print()
    
        


number = int(input("Enter number: "))

if __name__ == "__main__":
    pattern(number)

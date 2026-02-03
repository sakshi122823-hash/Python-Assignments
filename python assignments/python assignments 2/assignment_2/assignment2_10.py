def sum_digit(num):
    total = 0
    while num > 0:
        digit = num % 10      
        total = total + digit
        num = num // 10       
    print(total)

number = int(input("enter the number: "))
if __name__ == "__main__":
    sum_digit(number)

num = int(input("Enter a number: "))

divisible = lambda x : "true" if x % 5 == 0 else "false"
print(divisible(num))
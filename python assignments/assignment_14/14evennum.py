num = int(input("Enter a number: "))

even = lambda x : "true" if x % 2 == 0 else "false"
print(even(num))
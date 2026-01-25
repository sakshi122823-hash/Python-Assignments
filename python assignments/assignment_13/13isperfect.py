
def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
    return s == n

num = int(input("Enter a number: "))

result = is_perfect(num)   
if result:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

def count_digits(n):
    count = 0
    while n > 0:
        count = count + 1
        n //= 10
    print(count)

num = int(input("Enter a number: "))
if __name__ == "__main__":
    count_digits(num)

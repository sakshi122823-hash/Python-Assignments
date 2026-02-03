import threading

def even_list(numbers):
    evens = []
    total = 0
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
            total = total + 1
    print("Even numbers:", evens)
    print("Sum of even numbers:", total)


def odd_list(numbers):
    odds = []
    total = 0
    for n in numbers:
        if n % 2 != 0:
            odds.append(n)
            total =total+1
    print("Odd numbers:", odds)
    print("Sum of odd numbers:", total)


if __name__ == "__main__":
    nums = [10, 15, 20, 25, 30, 35]

    t1 = threading.Thread(target=even_list, args=(nums,))
    t2 = threading.Thread(target=odd_list, args=(nums,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

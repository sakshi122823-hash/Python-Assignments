from functools import reduce


nums = list(map(int, input("Enter numbers separated by space: ").split()))
data = reduce(lambda x , y :x*y ,nums)
print(data)
nums = list(map(int, input("Enter numbers separated by space: ").split()))
data = list(filter(lambda x :x%2==0,nums))
print(data)
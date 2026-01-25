nums = list(map(int, input("Enter numbers separated by space: ").split()))
data = list(filter(lambda x :x%5==0 and x%3==0,nums))
print(data)
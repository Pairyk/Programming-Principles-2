_ = input()
nums = list(map(int, input().split()))
result = len(list(filter(lambda x: x % 2 == 0, nums)))
print(result)
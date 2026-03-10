_ = input()
nums = list(map(int, input().split()))

arr = list(filter(lambda x: x != 0, nums))
print(len(arr))
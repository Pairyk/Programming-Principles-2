_ = input()
letters = list(map(str, input().split()))
nums = list(map(str, input().split()))
value = input()

d1ct = dict(zip(letters, nums))

print(d1ct.get(value, "Not found"))


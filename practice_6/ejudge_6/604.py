_ = input()
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

safe = 0

for nam, nom in zip(num1, num2):
    safe += nam * nom

print(safe)
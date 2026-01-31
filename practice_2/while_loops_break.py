# Example 1
i = 1
while i <= 100:
    if i % 7 == 0:
        print("First number divisible by 7:", i)
        break
    i += 1

# Example 2
attempts = 0
while attempts < 5:
    password = "attempt" + str(attempts)
    if password == "attempt2":
        print("Correct password!")
        break
    attempts += 1

# Example 3
num = 1
while num <= 20:
    if num == 13:
        print("Found 13!")
        break
    num += 1

# Example 4
temp = 0
while True:
    temp += 5
    print("Temperature:", temp)
    if temp >= 30:
        print("Too hot! Stopping.")
        break

# Example 5
stock = 100
while stock > 0:
    stock -= 15
    print("Stock remaining:", stock)
    if stock <= 50:
        print("Low stock alert!")
        break

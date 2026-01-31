# Example 1
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

# Example 2
num = -5
while num < 5:
    num += 1
    if num < 0:
        continue
    print(num)

# Example 3
counter = 0
while counter < 15:
    counter += 1
    if counter % 3 == 0:
        continue
    print(counter)

# Example 4
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue
    print(x)

# Example 5
entry = 0
while entry < 8:
    entry += 1
    if entry == 3 or entry == 6:
        continue
    print("Processing entry", entry)

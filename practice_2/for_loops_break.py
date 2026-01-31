# Example 1
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)

# Example 2
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print("First even:", num)
        break

# Example 3
for letter in "Hello World":
    if letter == "W":
        print("Found W!")
        break
    print(letter)

# Example 4
for i in range(1, 100):
    if i > 10:
        break
    print(i)

# Example 5
for x in range(20):
    if x * x > 50:
        print("Stopping at", x)
        break
    print(x, "squared is", x * x)

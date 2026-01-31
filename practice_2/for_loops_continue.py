# Example 1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# Example 2
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)

# Example 3
for letter in "Hello":
    if letter in "aeiouAEIOU":
        continue
    print(letter)

# Example 4
for num in range(1, 15):
    if num % 3 == 0:
        continue
    print(num)

# Example 5
numbers = [-2, -1, 0, 1, 2, 3]
for n in numbers:
    if n < 0:
        continue
    print(n)

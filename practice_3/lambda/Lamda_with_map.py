# Example 1: Square all numbers in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

print(f"Original: {numbers}")
print(f"Squared: {squared}")
# map() applies lambda to each element


# Example 2: Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")


# Example 3: Extract specific data from list of dictionaries
users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]
names = list(map(lambda user: user['name'], users))
ages = list(map(lambda user: user['age'], users))

print(f"Names: {names}")
print(f"Ages: {ages}")


# Example 4: Format strings
prices = [19.99, 29.50, 5.75, 100.00]
formatted_prices = list(map(lambda p: f"${p:.2f}", prices))

print(f"Original: {prices}")
print(f"Formatted: {formatted_prices}")


# Example 5: Apply multiple transformations
words = ['hello', 'world', 'python']
transformed = list(map(lambda w: w.upper().replace('O', '0'), words))

print(f"Original: {words}")
print(f"Transformed: {transformed}")


# Example 6: Map with multiple iterables
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
combined = list(map(lambda x, y: x + y, list1, list2))

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Sum: {combined}")
# map() can work with multiple iterables
# Example 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original: {numbers}")
print(f"Even numbers: {evens}")
# filter() keeps elements where lambda returns True


# Example 2: Filter numbers greater than threshold
scores = [45, 78, 92, 34, 88, 67, 95, 52]
passing_scores = list(filter(lambda score: score >= 60, scores))

print(f"All scores: {scores}")
print(f"Passing: {passing_scores}")


# Example 3: Filter strings by length
words = ['cat', 'elephant', 'dog', 'butterfly', 'ox', 'tiger']
long_words = list(filter(lambda word: len(word) > 4, words))

print(f"All words: {words}")
print(f"Long words: {long_words}")


# Example 4: Filter dictionaries by condition
products = [
    {'name': 'Laptop', 'price': 999, 'in_stock': True},
    {'name': 'Mouse', 'price': 25, 'in_stock': False},
    {'name': 'Keyboard', 'price': 75, 'in_stock': True},
    {'name': 'Monitor', 'price': 300, 'in_stock': False}
]
available = list(filter(lambda p: p['in_stock'], products))

print("Available products:")
for product in available:
    print(f"{product['name']} - ${product['price']}")


# Example 5: Filter with multiple conditions
ages = [15, 22, 17, 35, 42, 19, 28, 16]
young_adults = list(filter(lambda age: 18 <= age <= 30, ages))

print(f"All ages: {ages}")
print(f"Young adults (18-30): {young_adults}")


# Example 6: Remove empty strings and None values
mixed_data = ['hello', '', 'world', None, 'python', '', None, 'code']
cleaned = list(filter(lambda x: x, mixed_data))

print(f"Original: {mixed_data}")
print(f"Cleaned: {cleaned}")
# Empty strings and None are falsy, so they're filtered out
# ============================================================================
# TOPIC 1: ITERATORS - iter() and next()
# ============================================================================

# Example 1: Basic iter() and next() with a list
print("\n1. Basic iter() and next() with a list")
numbers = [10, 20, 30, 40, 50]
iterator = iter(numbers)
print(f"First call to next(): {next(iterator)}")
print(f"Second call to next(): {next(iterator)}")
print(f"Third call to next(): {next(iterator)}")


# Example 2: Looping through iterator with next() until StopIteration
print("\n2. Looping until StopIteration exception")
colors = ['red', 'green', 'blue']
color_iter = iter(colors)
try:
    while True:
        color = next(color_iter)
        print(f"Color: {color}")
except StopIteration:
    print("Finished iterating through all colors")


# Example 3: iter() with a string
print("\n3. Iterating through a string")
text = "Python"
text_iter = iter(text)
print(f"First: {next(text_iter)}, Second: {next(text_iter)}, Third: {next(text_iter)}")


# Example 4: iter() with a dictionary
print("\n4. Iterating through dictionary keys")
person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
dict_iter = iter(person)
print(f"First key: {next(dict_iter)}")
print(f"Second key: {next(dict_iter)}")
print(f"Third key: {next(dict_iter)}")


# Example 5: iter() with a set
print("\n5. Iterating through a set")
fruits = {'apple', 'banana', 'cherry'}
set_iter = iter(fruits)
print(f"First: {next(set_iter)}")
print(f"Second: {next(set_iter)}")
print(f"Third: {next(set_iter)}")


# Example 6: iter() with range object
print("\n6. Iterating through range")
range_iter = iter(range(5, 10))
print(f"Values: {next(range_iter)}, {next(range_iter)}, {next(range_iter)}")

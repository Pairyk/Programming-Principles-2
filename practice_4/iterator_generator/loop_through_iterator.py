# ============================================================================
# TOPIC 2: LOOP THROUGH AN ITERATOR
# ============================================================================

# Example 1: For loop (most common way to iterate)
print("\n1. Using for loop with iterator")
squares = [1, 4, 9, 16, 25]
for num in squares:
    print(f"Square root candidate: {num}")


# Example 2: While loop with next() and exception handling
print("\n2. While loop with next() and exception handling")
data = [100, 200, 300]
data_iter = iter(data)
while True:
    try:
        value = next(data_iter)
        print(f"Processing: {value}")
    except StopIteration:
        break


# Example 3: Unpacking iterator values
print("\n3. Unpacking multiple values from iterator")
pair_iter = iter(['Alice', 'Bob'])
name1, name2 = pair_iter
print(f"Names: {name1}, {name2}")


# Example 4: Using list() to consume entire iterator
print("\n4. Converting iterator to list")
letters = ['a', 'b', 'c', 'd']
letters_iter = iter(letters)
all_letters = list(letters_iter)
print(f"All letters: {all_letters}")


# Example 5: Using enumerate() with iterator
print("\n5. Using enumerate() with iterator")
items = ['first', 'second', 'third']
for index, item in enumerate(items):
    print(f"Index {index}: {item}")
    

# Example 6: Using zip() to combine iterators
print("\n6. Using zip() to combine multiple iterators")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

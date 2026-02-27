# ============================================================================
# TOPIC 4: GENERATORS - yield KEYWORD
# ============================================================================

# Example 1: Simple generator with yield
print("\n1. Simple generator yielding numbers")
def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(f"Generated: {value}")


# Example 2: Generator with yield in a loop
print("\n2. Generator yielding squares")
def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

print(f"Squares 1-5: {list(squares(5))}")


# Example 3: Generator with yield and conditional logic
print("\n3. Generator yielding only even numbers")
def even_numbers(max_num):
    for i in range(2, max_num + 1, 2):
        yield i

print(f"Even numbers up to 10: {list(even_numbers(10))}")

# Example 4: Generator that yields strings
print("\n4. Generator yielding countdown messages")
def countdown(start):
    while start > 0:
        yield f"T-minus {start}"
        start -= 1
    yield "Blastoff!"

for message in countdown(3):
    print(f"  {message}")

# Example 5: Generator with multiple yield statements
print("\n5. Generator yielding multiple values per iteration")
def pairs():
    yield 1, 'one'
    yield 2, 'two'
    yield 3, 'three'

for num, word in pairs():
    print(f"Number: {num}, Word: {word}")

# Example 6: Generator that processes and yields data
print("\n6. Generator processing list data")
def process_numbers(numbers):
    for num in numbers:
        yield num * 10

data = [1, 2, 3, 4, 5]
print(f"Processed: {list(process_numbers(data))}")
# ============================================================================
# TOPIC 6: GENERATOR EXPRESSIONS
# ============================================================================

# Example 1: Basic generator expression vs list comprehension
print("\n1. Generator expression (memory efficient)")
numbers = range(1, 6)
gen_expr = (x ** 2 for x in numbers)
print(f"Generator type: {type(gen_expr)}")
print(f"Values: {list(gen_expr)}")


# Example 2: Generator expression with conditional
print("\n2. Generator expression with condition")
numbers = range(1, 11)
even_squares = (x ** 2 for x in numbers if x % 2 == 0)
print(f"Even squares: {list(even_squares)}")

# Example 3: Comparison of memory usage
print("\n3. Memory comparison (list vs generator)")
list_comp = [x * 2 for x in range(5)]
gen_expr = (x * 2 for x in range(5))
print(f"List comprehension: {list_comp}")
print(f"Generator expression: {list(gen_expr)}")

# Example 4: Generator expression in a function argument
print("\n4. Generator expression passed to function")
numbers = [1, 2, 3, 4, 5]
result = sum(x ** 2 for x in numbers)
print(f"Sum of squares: {result}")

# Example 5: Nested generator expression
print("\n5. Nested generator expression")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = (num for row in matrix for num in row)
print(f"Flattened: {list(flattened)}")

# Example 6: Generator expression with string transformation
print("\n6. Generator expression transforming strings")
words = ['hello', 'world', 'python']
uppercase = (word.upper() for word in words)
print(f"Uppercase: {list(uppercase)}")

# Example 7: Generator expression with multiple conditions
print("\n7. Generator expression with multiple conditions")
numbers = range(1, 21)
filtered = (x for x in numbers if x % 2 == 0 if x > 5)
print(f"Even numbers greater than 5: {list(filtered)}")

# Example 8: Generator expression with transformation
print("\n8. Generator expression with tuple transformation")
names = ['Alice', 'Bob', 'Charlie']
name_lengths = ((name, len(name)) for name in names)
print(f"Names with lengths: {list(name_lengths)}")


# ============================================================================
# BONUS: PRACTICAL COMPARISON AND USE CASES
# ============================================================================

print("\n" + "=" * 70)
print("BONUS: PRACTICAL USE CASES")
print("=" * 70)

# Use case 1: Processing large files with generator
print("\n1. Simulating large file processing with generator")
def process_large_file():
    for line_num in range(1, 6):
        yield f"Line {line_num}: data"

for line in process_large_file():
    print(f"  {line}")

# Use case 2: Pipeline processing with generators
print("\n2. Pipeline processing with multiple generators")
def numbers_gen():
    for i in range(1, 6):
        yield i

def doubled(gen):
    for num in gen:
        yield num * 2

def squared(gen):
    for num in gen:
        yield num ** 2

result = squared(doubled(numbers_gen()))
print(f"Pipeline result (double then square): {list(result)}")

# Use case 3: Lazy evaluation benefit
print("\n3. Lazy evaluation - calculating only what's needed")
def expensive_computation():
    for i in range(1, 1001):
        print(f"  Computing value {i}...")
        yield i ** 2

gen = expensive_computation()
first_three = [next(gen) for _ in range(3)]
print(f"Only computed first 3: {first_three}")

print("\n" + "=" * 70)
print("END OF EXAMPLES")
print("=" * 70)
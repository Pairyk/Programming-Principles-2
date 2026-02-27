# ============================================================================
# TOPIC 5: CREATING GENERATOR FUNCTIONS
# ============================================================================

# Example 1: Infinite sequence generator
print("\n1. Infinite sequence generator (first 5 values)")
def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

counter_gen = infinite_counter()
first_five = [next(counter_gen) for _ in range(5)]
print(f"First five: {first_five}")


# Example 2: Generator for reading file-like data
print("\n2. Generator simulating file reading")
def read_chunks(text, chunk_size):
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size]

text = "ABCDEFGHIJ"
print(f"Chunks of 3: {list(read_chunks(text, 3))}")


# Example 3: Generator using send()
print("\n3. Generator using send() method")
def echo_generator():
    received = None
    while True:
        received = yield received
        print(f"  Generator received: {received}")

echo = echo_generator()
next(echo)  # Prime the generator
echo.send("Hello")
echo.send("World")


# Example 4: Generator that combines multiple sequences
print("\n4. Generator combining two lists")
def merge_lists(list1, list2):
    for item in list1:
        yield item
    for item in list2:
        yield item

combined = list(merge_lists([1, 2, 3], [4, 5, 6]))
print(f"Merged: {combined}")

# Example 5: Generator with state preservation
print("\n5. Generator preserving state across calls")
def sequence_generator():
    value = 10
    while value <= 15:
        yield value
        value += 1

gen = sequence_generator()
print(f"First value: {next(gen)}")
print(f"Second value: {next(gen)}")
print(f"Remaining: {list(gen)}")

# Example 6: Generator with try-finally for cleanup
print("\n6. Generator with resource management")
def resource_generator(items):
    try:
        for item in items:
            print(f"  Processing: {item}")
            yield item
    finally:
        print("  Cleanup complete!")

gen = resource_generator(['A', 'B', 'C'])
for value in gen:
    pass
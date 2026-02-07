# Example 1: Simple lambda function (one parameter)
square = lambda x: x ** 2

print(f"square(5) = {square(5)}")
print(f"square(10) = {square(10)}")
# Lambda syntax: lambda parameter: expression


# Example 2: Lambda with multiple parameters
add = lambda x, y: x + y
multiply = lambda x, y, z: x * y * z

print(f"add(3, 7) = {add(3, 7)}")
print(f"multiply(2, 3, 4) = {multiply(2, 3, 4)}")
# Syntax: lambda param1, param2, ...: expression


# Example 3: Lambda with conditional expression
max_of_two = lambda a, b: a if a > b else b

print(f"max_of_two(15, 8) = {max_of_two(15, 8)}")
print(f"max_of_two(5, 12) = {max_of_two(5, 12)}")
# Ternary operator: value_if_true if condition else value_if_false


# Example 4: Lambda for string operations
reverse_string = lambda s: s[::-1]
uppercase = lambda text: text.upper()

print(f"reverse_string('hello') = {reverse_string('hello')}")
print(f"uppercase('python') = {uppercase('python')}")


# Example 5: Lambda with default parameters
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))
# Default parameters work just like regular functions


# Example 6: Immediately Invoked Lambda Expression (IILE)
result = (lambda x, y: x * y)(5, 3)
print(f"(lambda x, y: x * y)(5, 3) = {result}")
# Lambda can be called immediately without assigning to variable
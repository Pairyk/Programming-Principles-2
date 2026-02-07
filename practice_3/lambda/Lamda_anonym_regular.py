# Example 1: Same functionality, different syntax
# Regular function
def regular_square(x):
    return x ** 2

# Lambda function
lambda_square = lambda x: x ** 2

print(f"Regular function: regular_square(5) = {regular_square(5)}")
print(f"Lambda function: lambda_square(5) = {lambda_square(5)}")


# Example 2: When to use regular functions (complex logic)
# Regular function - readable for complex logic
def calculate_discount(price, customer_type):
    """Calculate discount based on customer type"""
    if customer_type == 'VIP':
        discount = 0.20
    elif customer_type == 'Member':
        discount = 0.10
    else:
        discount = 0.05
    return price * (1 - discount)

# Lambda - NOT recommended for complex logic
# lambda_discount = lambda price, type: price * 0.8 if type == 'VIP' else price * 0.9 if type == 'Member' else price * 0.95
# ↑ Hard to read and maintain!
print(f"VIP price ($100): ${calculate_discount(100, 'VIP')}")
print(f"Member price ($100): ${calculate_discount(100, 'Member')}")
print("Lambda would be too complex here!")


# Example 3: Lambda for simple one-time use
# Regular function - overkill for one-time use
def add_ten(x):
    return x + 10

numbers = [1, 2, 3, 4, 5]
result_regular = list(map(add_ten, numbers))

# Lambda - perfect for one-time use
result_lambda = list(map(lambda x: x + 10, numbers))

print(f"Numbers: {numbers}")
print(f"With regular function: {result_regular}")
print(f"With lambda (better): {result_lambda}")
print("Lambda is cleaner for simple, one-time operations")


# Example 4: Documentation and naming
# Regular function - can have docstring
def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9

# Lambda - no docstring possible
to_celsius = lambda f: (f - 32) * 5/9

print(f"Regular function (with docstring): {convert_to_celsius(100):.1f}°C")
print(f"Lambda (no docstring): {to_celsius(100):.1f}°C")
print(f"Regular function docstring: {convert_to_celsius.__doc__[:50]}...")
print(f"Lambda docstring: {to_celsius.__doc__}")


# Example 5: Multiple statements
# Regular function - can have multiple statements
def process_text(text):
    """Process text with multiple steps"""
    text = text.strip()
    text = text.lower()
    text = text.replace(' ', '_')
    return text

# Lambda - only ONE expression allowed
# lambda_process = lambda text: ??? (Can't do multiple statements!)

input_text = "  Hello World  "
print(f"Input: '{input_text}'")
print(f"Processed: '{process_text(input_text)}'")
print("Lambda can't do multiple statements - use regular function!")


# Example 6: When each is best
# Best for Lambda:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"\n✓ Lambda is best for: {doubled}")
print("  - Simple, one-line operations")
print("  - One-time use with map(), filter(), sorted()")
print("  - Mathematical transformations")

# Best for Regular Functions:
def validate_email(email):
    """Validate email format"""
    if '@' not in email:
        return False
    if '.' not in email.split('@')[1]:
        return False
    return True

print(f"\n✓ Regular function is best for: validate_email('test@email.com') = {validate_email('test@email.com')}")
print("  - Complex logic with multiple conditions")
print("  - Need documentation (docstrings)")
print("  - Reusable code across your program")
print("  - Multiple statements or lines")
print("  - Better readability and debugging")
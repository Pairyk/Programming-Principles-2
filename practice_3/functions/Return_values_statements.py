# Example 1: Simple return value
def multiply(x, y):
    return x * y

result = multiply(7, 6)
print(f"7 × 6 = {result}")


# Example 2: Return multiple values (as tuple)
def calculate_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average  # Returns tuple

data = [10, 20, 30, 40, 50]
min_val, max_val, avg_val = calculate_stats(data)
print(f"Data: {data}")
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val}")


# Example 3: Conditional returns
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(f"Score 95: Grade {get_grade(95)}")
print(f"Score 82: Grade {get_grade(82)}")
print(f"Score 58: Grade {get_grade(58)}")


# Example 4: Return different data types
def analyze_text(text):
    return {
        'length': len(text),
        'words': len(text.split()),
        'uppercase': text.upper(),
        'lowercase': text.lower()
    }

result = analyze_text("Hello World Python")
for key, value in result.items():
    print(f"{key}: {value}")


# Example 5: Early return for validation
def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"  # Early return
    return a / b

print(f"10 / 2 = {divide_numbers(10, 2)}")
print(f"10 / 0 = {divide_numbers(10, 0)}")


# Example 6: Return None (implicit and explicit)
def print_banner(message):
    print("*" * 40)
    print(message.center(40))
    print("*" * 40)
    # No return statement = returns None

def validate_age(age):
    if age < 0 or age > 150:
        return None  # Explicit None
    return age

result1 = print_banner("Welcome!")
print(f"print_banner returned: {result1}")
print(f"validate_age(25): {validate_age(25)}")
print(f"validate_age(200): {validate_age(200)}")
# Example 1
has_license = True
has_car = True
can_drive = has_license and has_car
print(can_drive)

# Example 2
is_weekend = False
is_holiday = True
can_rest = is_weekend or is_holiday
print(can_rest)

# Example 3
is_raining = False
is_sunny = not is_raining
print(is_sunny)

# Example 4
age = 25
has_ticket = True
can_enter = (age >= 18) and has_ticket
print(can_enter)

# Example 5
x = 10
y = 20
z = 15
result = (x < y) and (y > z) or (x == z)
print(result)

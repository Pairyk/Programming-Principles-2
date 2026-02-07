# Example 1: Sort by absolute value
numbers = [-5, 2, -8, 1, -3, 7, -1, 4]
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))

print(f"Original: {numbers}")
print(f"Sorted by abs: {sorted_by_abs}")
# key parameter tells sorted() what to sort by


# Example 2: Sort strings by length
words = ['python', 'is', 'awesome', 'and', 'powerful']
sorted_by_length = sorted(words, key=lambda w: len(w))

print(f"Original: {words}")
print(f"Sorted by length: {sorted_by_length}")


# Example 3: Sort tuples by second element
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
sorted_by_grade = sorted(students, key=lambda student: student[1], reverse=True)

print("Original:", students)
print("Sorted by grade:")
for name, grade in sorted_by_grade:
    print(f"{name}: {grade}")


# Example 4: Sort dictionaries by value
inventory = [
    {'item': 'Apple', 'quantity': 50},
    {'item': 'Banana', 'quantity': 30},
    {'item': 'Orange', 'quantity': 75},
    {'item': 'Grape', 'quantity': 20}
]
sorted_inventory = sorted(inventory, key=lambda x: x['quantity'])

print("Sorted by quantity:")
for item in sorted_inventory:
    print(f"{item['item']}: {item['quantity']}")


# Example 5: Sort by multiple criteria
employees = [
    {'name': 'Alice', 'dept': 'IT', 'salary': 70000},
    {'name': 'Bob', 'dept': 'HR', 'salary': 60000},
    {'name': 'Charlie', 'dept': 'IT', 'salary': 80000},
    {'name': 'David', 'dept': 'HR', 'salary': 65000}
]
# Sort by department, then by salary (descending)
sorted_employees = sorted(employees, key=lambda e: (e['dept'], -e['salary']))

for emp in sorted_employees:
    print(f"{emp['name']} - {emp['dept']}: ${emp['salary']}")


# Example 6: Sort by last character of string
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
sorted_by_last = sorted(fruits, key=lambda s: s[-1])

print(f"Original: {fruits}")
print(f"Sorted by last char: {sorted_by_last}")
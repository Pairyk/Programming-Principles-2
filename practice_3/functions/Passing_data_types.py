# Example 1: Passing and modifying a list
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"Added '{item}' to list")

groceries = ["milk", "bread"]
print(f"Before: {groceries}")
add_item(groceries, "eggs")
add_item(groceries, "cheese")
print(f"After: {groceries}")  # Original list is modified!


# Example 2: Passing immutable types (strings, numbers, tuples)
def try_modify_string(text):
    text = text + " MODIFIED"
    print(f"Inside function: {text}")
    return text

original = "Hello"
print(f"Before: {original}")
result = try_modify_string(original)
print(f"After function: {original}")  # Original unchanged
print(f"Returned value: {result}")


# Example 3: Working with dictionaries
def update_player_score(player_dict, points):
    player_dict['score'] += points
    player_dict['games_played'] += 1

player = {'name': 'Alice', 'score': 100, 'games_played': 5}
print(f"Before: {player}")
update_player_score(player, 50)
print(f"After: {player}")


# Example 4: Processing list of numbers
def get_even_numbers(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return evens

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = get_even_numbers(numbers)
print(f"Original: {numbers}")
print(f"Even numbers: {even_nums}")


# Example 5: Nested lists
def sum_matrix(matrix):
    total = 0
    for row in matrix:
        for num in row:
            total += num
    return total

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix: {grid}")
print(f"Sum of all elements: {sum_matrix(grid)}")


# Example 6: Passing sets
def find_common_elements(set1, set2):
    return set1 & set2  # Set intersection

favorites1 = {"pizza", "burgers", "pasta", "sushi"}
favorites2 = {"sushi", "tacos", "pizza", "salad"}
common = find_common_elements(favorites1, favorites2)
print(f"Person 1 likes: {favorites1}")
print(f"Person 2 likes: {favorites2}")
print(f"Both like: {common}")


# Example 7: Avoiding list modification with slicing
def sort_list_copy(numbers):
    sorted_list = sorted(numbers)  # Creates new list
    return sorted_list

original_list = [5, 2, 8, 1, 9]
print(f"Original: {original_list}")
sorted_version = sort_list_copy(original_list)
print(f"Sorted: {sorted_version}")
print(f"Original unchanged: {original_list}")


# Example 8: Default mutable argument pitfall
def add_to_list_bad(item, my_list=[]):  # DANGEROUS!
    my_list.append(item)
    return my_list

def add_to_list_good(item, my_list=None):  # CORRECT
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print("Bad approach:")
print(add_to_list_bad("a"))  # ['a']
print(add_to_list_bad("b"))  # ['a', 'b'] - BUG! Shared list
print("\nGood approach:")
print(add_to_list_good("a"))  # ['a']
print(add_to_list_good("b"))  # ['b'] - New list each time

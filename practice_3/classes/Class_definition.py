# Example 1: Simple class with no attributes or methods
class EmptyBox:
    pass

box1 = EmptyBox()  
box2 = EmptyBox()  
print(f"box1 is an instance of EmptyBox: {isinstance(box1, EmptyBox)}")
print(f"box1 and box2 are different objects: {box1 is not box2}")


# Example 2: Class with attributes set after creation
class Person:
    pass

person1 = Person()
person1.name = "Alice"  
person1.age = 25
print(f"Person: {person1.name}, Age: {person1.age}")


# Example 3: Creating multiple objects from the same class
class Dog:
    species = "Canis familiaris"

dog1 = Dog()
dog1.name = "Buddy"
dog1.breed = "Golden Retriever"

dog2 = Dog()
dog2.name = "Max"
dog2.breed = "German Shepherd"

print(f"Dog 1: {dog1.name} - {dog1.breed}")
print(f"Dog 2: {dog2.name} - {dog2.breed}")
print(f"Both are: {Dog.species}")


# Example 4: Class with methods (preview)
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()  
result = calc.add(5, 3) 
print(f"5 + 3 = {result}")


# Example 5: Understanding object identity
class Car:
    pass

print("\nExample 5: Object identity")
car1 = Car()
car2 = Car()
car3 = car1 

print(f"car1 is car2: {car1 is car2}")  # Different objects
print(f"car1 is car3: {car1 is car3}")  # Same object
print(f"car1 id: {id(car1)}")
print(f"car2 id: {id(car2)}")
print(f"car3 id: {id(car3)}")


# Example 6: Class naming conventions
class BankAccount:
    """Proper class naming convention"""
    pass

class shopping_cart:  # Not recommended
    """Incorrect naming (snake_case)"""
    pass

account = BankAccount()
print(f"Class name: {BankAccount.__name__}")
print("Use PascalCase for class names (BankAccount, not shopping_cart)")


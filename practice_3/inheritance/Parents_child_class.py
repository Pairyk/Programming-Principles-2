# Example 1: Basic inheritance
class Animal:  # Parent class (base class)
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):  # Child class inherits from Animal
    pass

dog = Dog("Buddy")
dog.speak()  # Uses inherited method from Animal
print(f"Dog's name: {dog.name}")  # Uses inherited attribute


# Example 2: Child class with additional attributes
class Employee:  # Parent class
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def display_info(self):
        print(f"Employee: {self.name} (ID: {self.employee_id})")

class Developer(Employee):  # Child class
    def __init__(self, name, employee_id, programming_language):
        # Call parent constructor
        Employee.__init__(self, name, employee_id)
        # Add child-specific attribute
        self.programming_language = programming_language
    
    def code(self):
        print(f"{self.name} is coding in {self.programming_language}")

dev = Developer("Alice", "DEV001", "Python")
dev.display_info()  # Inherited method
dev.code()  # Child-specific method


# Example 3: Multiple child classes from same parent
class Vehicle:  # Parent class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        print(f"{self.brand} {self.model}")

class Car(Vehicle):  # First child
    def __init__(self, brand, model, doors):
        Vehicle.__init__(self, brand, model)
        self.doors = doors

class Motorcycle(Vehicle):  # Second child
    def __init__(self, brand, model, cc):
        Vehicle.__init__(self, brand, model)
        self.cc = cc

car = Car("Toyota", "Camry", 4)
bike = Motorcycle("Harley", "Street 750", 750)
car.info()
print(f"  Doors: {car.doors}")
bike.info()
print(f"  Engine: {bike.cc}cc")


# Example 4: Checking inheritance relationships
class Shape:
    pass

class Circle(Shape):
    pass

class Rectangle(Shape):
    pass

circle = Circle()
rectangle = Rectangle()

print(f"circle is instance of Circle: {isinstance(circle, Circle)}")
print(f"circle is instance of Shape: {isinstance(circle, Shape)}")
print(f"Circle is subclass of Shape: {issubclass(Circle, Shape)}")
print(f"Rectangle is subclass of Shape: {issubclass(Rectangle, Shape)}")


# Example 5: Multilevel inheritance (grandparent, parent, child)
class LivingBeing:  # Grandparent
    def __init__(self, name):
        self.name = name
        self.alive = True

class Animal(LivingBeing):  # Parent
    def __init__(self, name, species):
        LivingBeing.__init__(self, name)
        self.species = species

class Dog(Animal):  # Child
    def __init__(self, name, breed):
        Animal.__init__(self, name, "Canine")
        self.breed = breed

dog = Dog("Max", "Golden Retriever")
print(f"Name: {dog.name}")  # From LivingBeing
print(f"Species: {dog.species}")  # From Animal
print(f"Breed: {dog.breed}")  # From Dog
print(f"Alive: {dog.alive}")  # From LivingBeing


# Example 6: Inheritance with class variables
class University:  # Parent
    institution_type = "Educational"  # Class variable
    
    def __init__(self, name):
        self.name = name

class Department(University):  # Child
    def __init__(self, name, department_name):
        University.__init__(self, name)
        self.department_name = department_name

dept = Department("MIT", "Computer Science")
print(f"Department: {dept.department_name} at {dept.name}")
print(f"Institution type: {dept.institution_type}")  # Inherited class variable
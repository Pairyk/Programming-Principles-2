# Example 1: Basic difference between class and instance variables
class Dog:
    species = "Canis familiaris"  # Class variable (shared by all instances)
    def __init__(self, name, age):
        self.name = name  # Instance variable (unique to each instance)
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"Dog 1: {dog1.name}, {dog1.age} years - Species: {dog1.species}")
print(f"Dog 2: {dog2.name}, {dog2.age} years - Species: {dog2.species}")
print(f"Class variable accessed via class: {Dog.species}")


# Example 2: Modifying class variables affects all instances
class Counter:
    total_count = 0  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
        Counter.total_count += 1  # Modify class variable

c1 = Counter("Counter 1")
print(f"Total counters: {Counter.total_count}")
c2 = Counter("Counter 2")
print(f"Total counters: {Counter.total_count}")
c3 = Counter("Counter 3")
print(f"Total counters: {Counter.total_count}")
print(f"Accessed via instance: {c1.total_count}")


# Example 3: Instance variable shadows class variable
class Product:
    discount = 0.1  # Class variable (10% discount for all)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # self.discount is initially class variable

prod1 = Product("Laptop", 1000)
prod2 = Product("Mouse", 50)

print(f"{prod1.name}: ${prod1.price}, Discount: {prod1.discount}")
print(f"{prod2.name}: ${prod2.price}, Discount: {prod2.discount}")

# Create instance variable that shadows class variable
prod1.discount = 0.2  # Now prod1 has its own discount
print(f"\nAfter changing prod1 discount:")
print(f"{prod1.name} discount: {prod1.discount}")  # Instance variable
print(f"{prod2.name} discount: {prod2.discount}")  # Still class variable
print(f"Class discount: {Product.discount}")  # Unchanged


# Example 4: Using class variables for constants
class Pizza:
    SMALL = "Small (10 inch)"   # Class variables as constants
    MEDIUM = "Medium (12 inch)"
    LARGE = "Large (14 inch)"
    
    def __init__(self, size, toppings):
        self.size = size  # Instance variable
        self.toppings = toppings

pizza1 = Pizza(Pizza.LARGE, ["Pepperoni", "Mushrooms"])
pizza2 = Pizza(Pizza.SMALL, ["Cheese"])
print(f"Pizza 1: {pizza1.size} with {pizza1.toppings}")
print(f"Pizza 2: {pizza2.size} with {pizza2.toppings}")


# Example 5: Counting instances with class variables
class Employee:
    employee_count = 0  # Class variable
    
    def __init__(self, name, position):
        self.name = name  # Instance variables
        self.position = position
        self.id = Employee.employee_count + 1
        Employee.employee_count += 1
    
    @classmethod  # Class method to access class variable
    def get_employee_count(cls):
        return cls.employee_count

emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")
emp3 = Employee("Charlie", "Manager")

print(f"Employee 1: ID-{emp1.id}, {emp1.name} - {emp1.position}")
print(f"Employee 2: ID-{emp2.id}, {emp2.name} - {emp2.position}")
print(f"Employee 3: ID-{emp3.id}, {emp3.name} - {emp3.position}")
print(f"Total employees: {Employee.get_employee_count()}")


# Example 6: Class vs instance variables - complete example
class Website:
    total_visitors = 0  # Class variable - shared
    site_name = "MyWebsite"  # Class variable - shared
    
    def __init__(self, page_name):
        self.page_name = page_name  # Instance variable - unique
        self.page_views = 0  # Instance variable - unique
        Website.total_visitors += 1
    
    def visit(self):
        self.page_views += 1
        print(f"Visited {self.page_name}: {self.page_views} times")

home = Website("Home")
about = Website("About")
contact = Website("Contact")

home.visit()
home.visit()
about.visit()
contact.visit()
contact.visit()
contact.visit()

print(f"\nSite: {Website.site_name}")
print(f"Total visitors: {Website.total_visitors}")
print(f"Home page views: {home.page_views}")
print(f"About page views: {about.page_views}")
print(f"Contact page views: {contact.page_views}")

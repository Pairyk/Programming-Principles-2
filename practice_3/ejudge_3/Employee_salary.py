class Employee():
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def display(self):
        print(f"Name: {self.name}, Total: {self.base_salary:.2f}")


class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def display(self):
        print(f"Name: {self.name}, Total: {(self.base_salary + (self.base_salary/100)*self.bonus_percent):.2f}")


class Developer(Employee):
    def __init__(self, name, base_salary, projects):
        super().__init__(name, base_salary)
        self.projects = projects

    def display(self):
        print(f"Name: {self.name}, Total: {(self.base_salary + self.projects*500):.2f}")


class Intern(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

info = input()

if info.startswith("Developer"):
    role, name, base_salary, projects = info.split()
    worker = Developer(name, int(base_salary), int(projects)) 
    worker.display()
elif info.startswith("Manager"):
    role, name, base_salary, bonus = info.split()
    worker = Manager(name, int(base_salary), int(bonus))
    worker.display()
else:
    role, name, base_salary = info.split() 
    worker = Intern(name, int(base_salary))
    worker.display()


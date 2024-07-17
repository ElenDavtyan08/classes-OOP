print("\n" + 'ChatGPT exercises' + '\n') # just a seperator
# Exercises generated by chatGPT
# N1
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}")
        
    def bark(self):
        print(f"{self.name} is barking")
        
d1 = Dog('Bubble', 12, 'husky')
d1.bark()
d1.show_info()


#-------------------------------------------------------------------------------------
print() # just a seperator
# N2 Using Inheritance
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def Vehicle_info(self):
        print(f"Vehicle information -> Make: {self.make}, Model: {self.model}, Year: {self.year}")

    def is_vintage(self, current_year):
        self.current_year = current_year
        if (self.current_year - self.year) > 25:
            return f"Is vintage?: {True}"
        return f"Is vintage?: {False}"


class Car(Vehicle):
    def __init__(self, make, model, year, mass, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage
        self.mass = mass
        
    def drive(self, miles):
        self.miles = miles
        self.mileage += self.miles
        
    def get_info(self):
        print(f"CAR INFO - Make: {self.make}, Model: {self.model}, \nYear: {self.year}, Mass: {self.mass} tones, Mileage: {self.mileage} miles")

#running
car = Car('Tesla', 'Model X', 2020, 5, 105000)
car.drive(500)
car.get_info()
print(car.is_vintage(2024))

print() # just a seperator
truck = Vehicle('Mack', 'Model R', 1995)
truck.Vehicle_info()
print(truck.is_vintage(2024))

print() #just a seperator
#----------------------------------------------------------
# N3.
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        
    def __str__(self):
        return f"Name: {self.name}, ID: {self.emp_id}, Salary: ${self.salary}"
        
        
class Company:
    def __init__(self):
        self.employees = [] # list for employees
    
    # fire employee
    def hire_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} is hired")
        
    #fire employee    
    def fire_employee(self, employee_id):
        emp_to_fire = None
        for emp in self.employees:
            if emp.emp_id == employee_id:
                emp_to_fire = emp
                break
                
        if emp_to_fire:
            self.employees.remove(emp_to_fire)
            print(f'Employee {emp_to_fire.name} is fired')
        else:
            print(f"Employee with ID {employee_id} not found.")
    
    # raise salary with the give percentage
    def get_raise(self, emp_id, percentage):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.salary += emp.salary * (percentage/100)
                print(f"Employee {emp.name} received a {percentage}% raise.")
                return 
        print(f"Employee with ID {emp_id} not found.")
        
    # display all employees, if there are some
    def display_employees(self):
        if not self.employees:
            print('There is no employees in the company')
        else:
            for employee in self.employees:
                print(employee)
                
                
# run the program
company = Company()

emp_1 = Employee('John', 1, 15000)
emp_2 = Employee('Ann', 2, 20000)
emp_3 = Employee('Kate', 3, 10000)

company.hire_employee(emp_1)
company.hire_employee(emp_2)
company.hire_employee(emp_3)
print()
company.fire_employee(2)
print()
company.get_raise(3, 10)
company.get_raise(1, 20)
print()
company.display_employees()
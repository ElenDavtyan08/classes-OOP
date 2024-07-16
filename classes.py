# Here I just write some notes 'bout classes 

# Corey Schafer
class Employee:

    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
# running
"""emp_1 = Employee('Elen', 'Davtyan', 'el.davtyan08@gmail.com')
emp_2 = Employee('name', 'surname', 'namesurname@mail.ru')

print(Employee.fullname(emp_1))"""
# a = emp_1.fullname() The same output as it is in the line 14
# print(a)


##################################################
# tech with Tim
# first class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

dogs_name = ['Tim', 'Bill']
dogs_age = [32, 14]


####################################################
#multiple classes
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0 -100

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_averge_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
    
    def max_grade(self): # this method was added by me
        grades = []
        for student in self.students:
            grades.append(student.get_grade())
        return max(grades)

# running
"""s1 = Student('Elen', 16, 64)
s2 = Student('Bill', 16, 20)
s3 = Student('Jill', 16, 95)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_averge_grade())
print(course.max_grade())"""

######################################################3
# Inheritance
class Pet: # general, parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} yaers old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet): # inherit from Pet, child class
    def __init__(self, name, age, color):
        super().__init__(name, age) # superclass
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f"I am {self.name} and I am {self.age} yaers old and I am {self.color}")

class DogSecond(Pet): # child class
    def speak(self):
        print('Bark')

# running
"""p = Pet('Tim', 19)
p.speak()
c = Cat('Bill', 34, 'Brown')
c.show()
d = DogSecond('Jill', 25)
d.speak()"""


###########################################
#attributes
class Person:
    number_of_people = 0 #-> this is a class attribute, and it is specific to the class not the instance

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod # decorator to denote that it is a claasMethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

# running
"""
we can change its value like: Person.number_of_people = 8 --
-- print(p2.number_of_people) we will get 8 instead of 0
p1 = Person('tim')
p2 = Person('jill') 
print(Person.number_of_people_())
"""

#############################################
#static methods
class Math:
# if we want to use it like the module, \ 
# for exp: import math; math.sqrt()
    
    @staticmethod # -> not changing method
    def add5(x): # it will act just like a function
        return x+5
    
    @staticmethod
    def add10(x):
        return x+10
    
    @staticmethod
    def pr():
        print('Run')

# running   
Math.pr()

# This class, which is made by me, allows us to save our grades for entered subjects, \
# and we can also calculate the average grade for the subject we want
class School:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.subject_grade = {}
        
    def show(self):
        print(f"Name, Surname: {self.name} {self.surname}")
        
    def sub_grade(self, sub, grade):
        self.subject = sub
        self.grade = grade
        if not sub in self.subject_grade:
            self.subject_grade[self.subject] = [self.grade]
        else:
            self.subject_grade[self.subject].append(self.grade)
            
        return self.subject_grade
    
    def average(self, subject):
        self.sub = subject
        if self.sub in self.subject_grade:
            a = sum(self.subject_grade[self.sub]) / len(self.subject_grade[self.sub])
            return f"Average ({self.sub}): {a}"
        else:
            return 'There is no such subject'

# run the program
s1 = School('Kate', 'Brown')
name = s1.show()
s1.sub_grade('math', 19)
s1.sub_grade('math', 20)
print(s1.sub_grade('english', 19))
print('s1 -> ', s1.average('math'))

print() # just a seperator
s2 = School('Ann', 'Johnson')
name2 = s2.show()
s2.sub_grade('history', 20)
s2.sub_grade('geometry', 19)
s2.sub_grade('history', 19)
print(s2.sub_grade('history', 18))
print('s2 -> ', s2.average('history'))


#------------------------------------------------------------------
print('\n'+'Exercise No 2.')
# N2. The problem is generated by GPT, but was completely solved by me

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Grades: {self.grades}'
    
    def grade_avg(self):
        print(f"{self.name}'s grades average: {round(sum(self.grades)/len(self.grades), 2)}")
            
class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary
        
class SecondSchool:
    def __init__(self):
        self.students = []
        self.teachers = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        
    def remove_student(self, st_name):
        for i in self.students:
            if i.name == st_name:
                self.students.remove(i)
            else:
                print('There is no such student with that name.')
                
    def remove_teacher(self, tch_name):
        for j in self.teachers:
            if j.name == tch_name:
                self.teachers.remove(j)
            else:
                print('There is no such teacher with that name.')
                
    def display_students(self):
        for i in self.students:
            print(f'Name: {i.name}, Age: {i.age}, Grades: {i.grades}')
            
    def display_teachers(self):
        for j in self.teachers:
            print(f"Name: {j.name}, Subject: {j.subject}, Salary: ${j.salary}")


#running
school = SecondSchool()
student1 = Student("Alice", 14, [85, 90, 78])
student2 = Student("Bob", 15, [88, 92, 80])
teacher1 = Teacher("Mr. Smith", "Math", 50000)
teacher2 = Teacher("Ms. Johnson", "English", 55000)

school.add_student(student1)
school.add_student(student2)
school.add_teacher(teacher1)
school.add_teacher(teacher2)
school.display_students()
# Output:
# Name: Alice, Age: 14, Grades: [85, 90, 78]
# Name: Bob, Age: 15, Grades: [88, 92, 80]

student1.grade_avg()
student2.grade_avg()
#Output:
# Alice's grades average: 84.33
# Bob's grades average: 86.67

school.display_teachers()
# Output:
# Name: Mr. Smith, Subject: Math, Salary: $50000
# Name: Ms. Johnson, Subject: English, Salary: $55000

school.remove_student("Alice")
school.display_students()
# Output:
# Name: Bob, Age: 15, Grades: [88, 92, 80]

school.remove_teacher("Mr. Smith")
school.display_teachers()
# Output:
# Name: Ms. Johnson, Subject: English, Salary: $55000
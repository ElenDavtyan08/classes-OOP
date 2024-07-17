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
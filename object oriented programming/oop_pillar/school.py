class School :
    #constructor
    def __init__(self , name , address , principal = ''):
        self.name = name
        self.address = address 
        self.principal = principal
        self.grades = []

    def add_grade(self, name, teacher):
        new_grade = Grade(name, teacher)   
        self.grades.append(new_grade)
    def remove_grade(self, name):  
        idx = 0
        for i, grade in enumerate(self.grades):
            if grade.name == name:
               idx = i
        del self.grades[idx]         

class Grade:
    #constructor
    def __init__(self , name,teacher):
        self.students = []
        self.name = name
        self.teacher = teacher

    def __repr__(self) -> str:
        return f"{self.name} with  faculty {self.teacher}"  
    def __del__ (self):
        print(f'Deleting ${self.name} with teacher {self.teacher}') 
    


     
oxford = School("Oxford school", 'cumilla', 'Akib Zaman ') 
oxford.add_grade('class 4', 'Galib Zaman')
oxford.add_grade('class 5', 'Heme Mam')

print(oxford.grades)
oxford.remove_grade('class 5')
print(oxford.grades)
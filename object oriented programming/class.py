class Person:
    def __init__(self,person_name , person_age):
        self.name = person_name
        self.age = person_age

a_person =Person("Farhad",23)  
print(a_person.name)
print(a_person.age)



class Student:
    def __init__(self,student_name , student_age , student_class_name):
        self.name = student_name
        self.age = student_age
        self.cls= student_class_name
    def get_student(self):
      return f"Name: {self.name},age:{self.age}, class:{self.cls}"


a_student =Student("Farhana", "19" , "varsity") 

print(a_student.get_student())





# class Person:
#     def __init__(self,person_name , person_age):
#         self.name = person_name
#         self.age = person_age

# a_person =Person("Farhad",23)  
# print(a_person.name)
# print(a_person.age)



class Student:
    def __init__(self,student_name:str , student_age:int , student_class_name:int):
        self.__name = student_name
        self.__age = student_age
        self.cls= student_class_name
    
    def get_student_of_class(self):
        return self.cls
    def get_student_name(self):
        return self.__name    
    def set_name(self, new_name):
        if(self.has_any_number(new_name)):
            print("Sorry person name can't have number")
            return
        self.name = new_name 

    def has_any_number(self , string):
        return "0" in string      
    def get_student(self):
      return f"Name: {self.__name},age:{self.__age}, class:{self.cls}"

student_list = [Student("Farhana", 19 , 13),
Student("Farhad" , 23 , 15),
Student("Nuha" , 23 ,16)
] 

for student in student_list:
    if student.get_student_of_class()>=14:
        print(student.get_student())

# a_student =Student("Farhana", 19 , 13) 
# print(a_student.get_student())
# a_student.set_name("0Farhana")
# print(a_student.name)

class Aust_student(Student):
    def __init__(self,student_name:str , student_age:int , student_class_name:int,student_email:str ):
        super().__init__(student_name,student_email)
        self.name = student_name
        self.email = student_email
    def  get_student(self):
       return f"Name : {self.get_student_name()} Email : {self.email}"


aust_std =Aust_student("Nuha" , 23 ,16 , "farhad.aust@gmail.com")
print(aust_std.get_student())






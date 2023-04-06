class Student:
    def __init__(self, name ,age , id ):
        self.name = name
        self.age = age
        self.id = id

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

class Teacher:
    def __init__(self, name,course):
        self.name = name
        self.course = course

class School:
    def __init__(self, name , teachers,courses ,students):
        self.name = name
        self.teachers = teachers 
        self.course = courses
        self.students = students 
    def get_students(self):
        for student in self.students:
            print(student.name)


school_name = " AK Azad University"
data_science_course = Course( 'Data Science' , "Farhad Ahmed")
teacher_1 = Teacher("Farhad Ahmed" ,data_science_course)   
py_course = Course( 'python' , "Einstein")
teacher_2 = Teacher("Einstein" , py_course) 


student_1 = Student("Shkib khan " , 22 , 1011  )
student_2 = Student("Salman khan " , 55 , 1055  )
student_3 = Student("Amir khan " , 45 , 1066  )
student_4 = Student("Amir khan " , 45 , 1066  )

teachers = [teacher_1 , teacher_2]
courses = [data_science_course , py_course]
students =  [student_3, student_4]

my_school = School(school_name, students, courses , teachers)
# print(my_school.students)
my_school.get_students()





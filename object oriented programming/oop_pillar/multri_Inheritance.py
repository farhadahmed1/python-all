class School :
    def __init__(self ,school_name):
        self.school_name = school_name 
        print('School name class')

class Grader : 
    def __init__(self, grade_name):
        self.grade_name = grade_name
        print ('Grader name init called')

class Student(School , Grader):
    def __init__(self, name , grade_name, school_name):
        self.name = name

        Grader.__init__(self, grade_name)
        School.__init__(self, school_name)
        print('Student init Called' )



A_khan = Student('Ak' ,'Bsc' , 'USA school of lowered')
print(A_khan.name)
print(A_khan.school_name)
print(A_khan.grade_name)



                   
# class Person : 
#     def __init__(self, name ,age) :  
#         self.name = name
#         self.age = age
#     def __del__(self) :  
#         print("Object is being deleted")

# person =Person("Farhad" , 24)
# del person

# Magic Methods & Dunder

class vector:
    def __init__(self, x,y ) : 
        self.x = x
        self.y = y
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        return vector(self.x * other.x, self.y * other.y)
    def __sub__(self ,other):
        return vector(self.x - other.x , self.y -  other.y)
 

v1 =vector(212, 202)
v2 =vector(22, 20)
sum = v1 + v2
mul = v1 * v2
sub = v1 - v2
print(sum.y , mul.y )   
print(sub.x) 


class Employee :
    def __init__(self,name , id ,salary , position ):
        self.name = name
        self.id = id
        self.salary = salary
        self.position = position

class Developer (Employee): 
    def __init__(self,name , id ,salary , 
                 position , tech  , focus):    
        self.tech  = tech
        self.focus= focus
        super().__init__(name ,id , salary , position)
class Testing(Employee): 
    pass        

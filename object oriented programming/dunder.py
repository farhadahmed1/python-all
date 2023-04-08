class Person:
    def __init__(self,name , age , money , height =65):
        self.name = name 
        self.age = age
        self.money = money
        self.height = height\
        

    def _call_ (self ,other):
        return  f' This is  {self.name }  with aga {self.age} and have{self.money}'
    def _add_ (self ,other):
        return self.age + self.money + self.height
    
       
        

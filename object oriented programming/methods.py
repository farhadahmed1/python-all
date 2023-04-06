class Calculator : 
    def add(self,value1 , value2):
        return value1 + value2 
    def subtract(self,value1, value2):
        return value1 - value2
    def divide(self,value1, value2):
        return value1 / value2
    def multiply(self,value1, value2):   
        return value1 * value2


result = Calculator()
sum = result.subtract( 30,20)
print(sum)


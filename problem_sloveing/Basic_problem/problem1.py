name = input("Enter your name : ")
salary =input("Enter your salary: ")

# problem 1

def show_employee(nam=" " ,sal=9000):
    return f"employee name {nam} and  salary {sal}"

result =  show_employee( " ", 1242009)
print(result)


# problem 2
def calculate (num1 , num2 ):
    sum  = num1 + num2 
    mul  = num1 * num2
    subtract = num1 - num2 
    return f"addition value : {sum} subtraction value : {subtract} multiplication :{mul}"

result = calculate(10 ,2)    
print(result)



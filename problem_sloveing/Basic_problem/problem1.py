# name = input("Enter your name : ")
# salary =input("Enter your salary: ")

# # problem 1

# def show_employee(nam=" " ,sal=9000):
#     return f"employee name {nam} and  salary {sal}"

# result =  show_employee( " ", 1242009)
# print(result)


# # problem 2
# def calculate (num1 , num2 ):
#     sum  = num1 + num2 
#     mul  = num1 * num2
#     subtract = num1 - num2 
#     return f"addition value : {sum} subtraction value : {subtract} multiplication :{mul}"

# result = calculate(10 ,2)    
# print(result)



list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

result = [i + j for i, j in zip(list1 ,list2)]
print(result)

numbers = [1, 2, 3, 4, 5, 6, 7]
square_number = map(lambda num: num*num, numbers)
print(list(square_number)) 

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
result = [i ,j for i, j in zip(list1 ,list2)]








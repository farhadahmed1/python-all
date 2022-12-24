# def square (x):
#     return x*x
# result = square(6)  

x = int(input("enter the value of x : "))
y = int(input("enter the value of y : "))

square = lambda x: x*x
result = square(x)
print(result) 
# sum lambda function
add = lambda num1  , num2: num1+ num2
sum_result =add(x , y)
print(sum_result)

numbers =[23, 4, 5, 66, 78, 96,97,7,9,100, 663 ,754]

def double_it(num):
    return num *2 

square = lambda num : num* num    
# map (function , iterable)
doubled_number = map(double_it, numbers)
print(list(doubled_number)) 
# filter (function , iterable)
filter_number = filter(lambda num : num >=50 , numbers)
bigger_number = list(filter_number)
print(bigger_number)

square_number = map(lambda num: num*num, bigger_number)  
#square_number = map(square, numbers)      
print(list(square_number)) 


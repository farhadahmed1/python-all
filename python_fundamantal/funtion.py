# num  =int( input(" Enter the number : "))
# def double_it(num):
#     result = num * 2
#     print(result)
# double_it(num)
num1 = int (input(" Enter the num1 :"))
num2 = int (input(" Enter the num2 :"))
def add( num1 , num2 ):
    total = num1 + num2
    return total
sum  =  add(num1 ,num2)     
print (f"total sum value {sum}")


def multiply(num1, num2):
    result = num1 * num2
    return result

output = multiply(num1 , num2)    
print(f"Multiplying value {output}")

final_value  = add(sum , output)
print(f"final_value {final_value}")






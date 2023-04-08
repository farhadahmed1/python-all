import math
import  time 
def timer(func):
    def inner(*args, **kwargs):
        print('time start')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Time End . Total time taken {end-start}')
    return inner
# decorators
@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'factorial of {n} is {result}')
# timer(get_factorial)()      
get_factorial( n= 20)


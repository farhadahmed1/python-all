def do_something():
    print ('Starting to do something')
    def inner_function():
        print('Inside thr inner function')

    inner_function() 
# do_something()    
def first_function():
    print('Inside first function') 
    def second_function():
        print('Inside the inner function')
    return second_function
first = first_function()
first()
    
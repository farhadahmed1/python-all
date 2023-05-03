# laptop , phone , watch , computer

class  Device:
    def __init__(self ,brand , price , color):
        self.brand = brand 
        self.price = price 
        self.color = color

class Laptop (Device):
    def __init__(self ,brand, price , color , display_size  ):
        super().__init__(brand, price, color)
        self.display_size = display_size

    def run (self):
        print('Running the Laptop')

    def purchase (self , money ):
        if money <self.price:
            return 'No laptop for you'
        else:
            print('this device is for you')
            return money - self.price
        
class  Phone :
    def __init__(self ,brand, price , color,camera):
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera


class Watch : 
    def __init__(self ,brand, price , color ,watch_type) :
        self.brand = brand
        self.price = price
        self.color = color
        self.watch_type = watch_type

    def is_digital (self ):
        return self.watch_type == 'digital'
    

class Manager : 
    def __init__(self ,name , salary  ,  experience , 
                 designation ,): 
        pass 
    def day_total_sales(self):
        pass

class SalesPerson: 
    def __init__(self ,name , salary  ,  experience , 
                 designation , commission ): 
        pass   

    def handle_customer (self):
        pass

lenovo  = Laptop ('lenovo ' , 45000 , 'gray' , '1000Gb')   
print(lenovo.color) 




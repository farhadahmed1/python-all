#parent class
#base class
# class BaseClass :
#     pass

#child class
# derived class
# class DerivedClass(BaseClass) :
#     pass

# 1.  single inheritance
# 2. multi_level inheritance


class Vehicle: 
    def __init__(self ,name ,  license , price ) : 
        self.name = name 
        self.license = license
        self.price = price

    def start(self):
        print (f'{self.name} started')    

class   Bus (Vehicle):
    def __init__(self ,name , license , price, seat ,ticket_price) : 
        self.seat = seat
        self.available_seats = seat
        self.ticket_price = ticket_price

    def sell_tickets(self , quantity , customer_name , amount):
        self.available_seats -= quantity
        remainder = amount - self.ticket_price * quantity 
        
        if remainder >= 0 :
            return Ticket(customer_name)
        return 'No tickets available for you. you  '
        
class Ticket :
    def __init__(self , owner) -> None : 
        self.owner = owner


            


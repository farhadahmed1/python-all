class User: 
    def __init__(self , first_name , last_name):
        self.first  = first_name
        self.last = last_name
        self.email = f'{self.first}.{self.last}@user.com'
 
    @property
    def full_name(self):
        return f" {self.first} {self.last}"
    
    @full_name.setter
    def full_name(self , value):
        first , last = value.split (' ')
        self.first = first
        self.last = last
        self.email = f'{self.first}.{self.last}.@user.com'
    @full_name.deleter
    def full_name(self):
        del self.first
        del self.last    
    @property
    def get_email_address(self):
        return self.email
    
    # @get_email_address.setter
    # def get_email_address(self, value): 
    #     self.email =value.split(' ')[0]

mark  = User('mark', 'zukarbarg')  
print( mark.email)
print( mark.full_name)
# print( mark.get_email_address())
mark.full_name = 'Farhad ahmed'
print( mark.full_name)
print( mark.get_email_address)
# del mark.full_name
# # print(mark.first)
# mark.full_name = 'Salman khan'
# print(mark.full_name)
# print(mark.get_email_address)

class User: 
    def __init__(self, name, password , phone):
        self.name = name
        self.__password = password
        self.phone = phone

    def __get_password(self):
        print(self.__password)  

    def user_login(self , name, password):
        if(name == self.name and password == self.__password):
            return f' {self.name} logIn successful'
        return f' {self.name} your password is not correct' 
        
ryan= User ('Ryan Dal', 'dal123', '0187626')
print(ryan.name)
# ryan._get_password()
# print(ryan.password) 
user = ryan.user_login('Ryan Dal', 'dal124')   
print(user)    
class Phone:
    def __init__(self, brand, price, color ,model ): 
        self.brand = brand
        self.price = price
        self.color = color
        self.model = model

motherPhone  = Phone('Oppo', 12000, 'golden', 'A71'  )  
fatherPhone = Phone('Oppo', 15000, 'golden', 'V21' )             
print( f' Brand : {motherPhone.brand}, Price : {motherPhone.price} , Model : {motherPhone.model}')

print( f' Brand : {fatherPhone.brand}, Price : {fatherPhone.price} , Model : {fatherPhone.model}')
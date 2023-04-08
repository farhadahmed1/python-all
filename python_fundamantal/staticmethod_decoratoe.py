class Shopping :
    def __init__(self ,customer):
        self.customer = customer
        self.items = []
        self.total = 0
    
    def add_to_cart(self,items, price , quantity):
        self.items.append(items)

    def checkout(self):
        pass          
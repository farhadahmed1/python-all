class Shopper : 
    def __init__(self ,name):
        self.name = name
        self.card = []

    def add_to_card(self, item, price , quantity ):
        self.card.append({'item':item, 'price': price ,'quantity':quantity})  
    def checkOut(self , amount):
        print(self.card)
        price = 0 
        for item in self.card:
            print(item)
            price += item['price'] * item['quantity']
            print(price)
        if amount < price:
            return f'Please give me more money : {price - amount}'
        elif amount > price:
            return f'Here is the items and extra money : {amount- price}'
        else: 
            return ' Here are the items '

             





shopping = Shopper("Ahmed") 
shopping.add_to_card('pant', 1200 , 2)
shopping.add_to_card('shirt', 900 , 3)


reply = shopping.checkOut(6000)
print(reply)

# class Item:
#     def calculate_total_price():

# item1 = Item()
# item1.name = 'Phone'
# item1.price = 100
# item1.quantity = 5

# item2 = Item()
# item2.name = 'Laptop'
# item2.price = 65000
# item2.quantity = 1

class Item:
    pay_rate = 0.8  # This is a class attribute #The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):

        # run validations to receive arguments
        assert price >= 0, f'Given input is negative'
        assert quantity >= 0

        # print(f'An instance created: {name}')
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


# if you pass price here as str like this: '100' ,it won't throw you an error instead it will behave like string
item = Item('Phone', 100, 5)

# You can also add some more attributes like this ,it doesn't always have to made inside the method of the constructor
item.has_numpad = False
# print(item.calculate_total_price(item.price, item.quantity))

print(Item.pay_rate)

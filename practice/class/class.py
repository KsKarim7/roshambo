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

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


# if you pass price here as str like this: '100' ,it won't throw you an error instead it will behave like string
item = Item('Phone', 100, 5)
item2 = Item('Laptop', 250, 2)


item.apply_discount()
print(item.price)

# print(Item.__dict__)  # All the attributes for class level
# print(item2.__dict__)  # All the attributes for instance level

# You can also add some more attributes like this ,it doesn't always have to made inside the method of the constructor
# item.has_numpad = False
# print(item.calculate_total_price(item.price, item.quantity))


# item2 = Item('Laptop', 250, 2)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

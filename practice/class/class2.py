class Item:
    pay_rate = 0.8
    all = []

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
item2 = Item('PC', 550, 1)
item3 = Item('Mouse', 50, 4)
item4 = Item('Keyboard', 70, 6)
item5 = Item('Laptop', 250, 2)

print(Item.all)

for ins in Item.all:
    print(ins.name)

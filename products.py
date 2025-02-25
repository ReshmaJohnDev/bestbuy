class Product:
    def __init__(self, name, price, quantity):
        if name and price and quantity:
            if price >0 and quantity >0:
                self.name = name
                self.price = price
                self.quantity = quantity
                self.active = True
        else :
            raise Exception("Enter valid input")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):

        if self.active:
            return True
        else :
            return False

    def deactivate(self):
        self.active = False


    def activate(self):
        self.active = True


    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity} "

    def buy(self, quantity):
        self.quantity -=quantity
        self.set_quantity(self.quantity)
        return self.quantity


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)
print(bose.show())
print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())
print(bose.is_active())








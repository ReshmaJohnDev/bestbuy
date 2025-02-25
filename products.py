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
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else :
            self.activate()

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
        if quantity:
            total_price = float(self.price * quantity)
            self.quantity -= quantity
            self.set_quantity(self.quantity)
            return total_price

        else :
            raise Exception("Enter valid input")











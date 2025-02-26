class Product:
    """The Product class represents a specific type of
     product available in the store"""
    def __init__(self, name, price, quantity):
        """Initiator (constructor) method."""
        if not name or price <= 0 or quantity < 0:
            raise ValueError("Enter valid input: name must be non-empty,"
                             " price > 0, and quantity >= 0")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0


    def get_quantity(self):
        """Returns the quantity (int)"""
        return self.quantity


    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else :
            self.activate()


    def is_active(self):
        """Returns True if the product is active, otherwise False."""
        is_active = False
        if self.active:
            is_active = True
        return is_active


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def activate(self):
        """Activates the product."""
        self.active = True


    def show(self):
        """Returns a string that represents the product"""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price of the purchase.
        Updates the quantity of the product.
        """
        if quantity <= 0:
            raise ValueError("Enter a valid quantity (must be greater than 0)")

        if quantity > self.quantity:
            raise ValueError("Error while making order! Quantity larger than what exists")

        total_price = self.price * quantity
        self.quantity -= quantity
        self.set_quantity(self.quantity)
        return total_price

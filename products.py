from promotions import Promotion

class Product:
    """The Product class represents a specific type of
     product available in the store"""
    def __init__(self, name, price, quantity, promotion = None):
        """Initiator (constructor) method."""
        if not name or price <= 0 or quantity < 0:
            raise ValueError("Enter valid input: name must be non-empty,"
                             " price > 0, and quantity >= 0")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = promotion
        self.active = quantity >= 0
        self.backup_quantity = quantity


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
        return self.active


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def activate(self):
        """Activates the product."""
        self.active = True


    def show(self):
        """Returns a string that represents the product"""
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else None
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {promotion_info}"


    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price of the purchase.
        Updates the quantity of the product.
        """
        if quantity <= 0:
            raise ValueError("Enter a valid quantity (must be greater than 0)")

        elif quantity > self.quantity:
            raise ValueError("Error while making order! Quantity larger than what exists")

        total_price = (self.promotion.apply_promotion(self, quantity) if self.promotion else self.price * quantity)
        self.set_quantity(self.quantity - quantity)
        return total_price


    def get_promotion(self):
        return self.promotion

    def set_promotion(self,promotion):
        self.promotion = promotion


    def rollback_quantity(self):
        """Rolls back the quantity to the backed-up state."""
        self.quantity = self.backup_quantity
        self.set_quantity(self.quantity)
        if self.quantity > 0:  # Reactivate if there is any stock
            self.activate()
        else:  # Deactivate if quantity is 0
            self.deactivate()


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)


    def show(self):
        """Overrides the show method to display 'Unlimited' for quantity."""
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited, Promotion: {promotion_info}"


    def get_quantity(self):
        """Overrides get_quantity to always return 0."""
        return 0


    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        self.activate()


    def is_active(self):
        """Overrides is_active to always return True."""
        return True


    def buy(self, quantity):
        """
        Overrides buy method of parent class to update the quantity to 0
        """
        if quantity <= 0:
            raise ValueError("Enter a valid quantity (must be greater than 0)")

        total_price = (self.promotion.apply_promotion(self, quantity) if self.promotion else self.price * quantity)
        self.quantity = 0
        self.set_quantity(quantity)
        return total_price


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        self.maximum = maximum
        super().__init__(name, price, quantity)


    def show(self):
        """Overrides the show method to display 'Unlimited' for quantity."""
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else None
        return (f"{self.name}, Price: {self.price},"
                f" Limited to {self.maximum} per order!,"
                f" Promotion: {promotion_info}")


    def buy(self, quantity):
        """Overrides the buy method to update the quantity
        when quantity is greater than maximum"""
        if quantity <= 0:
            raise ValueError("Enter a valid quantity (must be greater than 0)")
        elif quantity > self.maximum:
            raise ValueError(f"Only {self.maximum} is allowed from this prod")
        total_price = (self.promotion.apply_promotion(self, quantity) if self.promotion else self.price * quantity)
        self.set_quantity(self.quantity - quantity)
        return total_price

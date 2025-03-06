class Store:
    """Store Class will hold all the products,
     and will allow the user to make a purchase of
     multiple products at once."""
    def __init__(self, product_list):
        """Initiator (constructor) method."""
        self.product_list = product_list


    def add_product(self, product):
        """Adds a product to the store."""
        if product not in self.product_list:
            self.product_list.append(product)


    def remove_product(self, product):
        """Remove products if it already exists in the store."""
        if product in self.product_list:
            self.product_list.remove(product)


    def get_total_quantity(self):
        """ Returns total quantity of products available in store"""
        return sum(product.get_quantity() for product in self.product_list)


    def order(self, shopping_list):
        """Process the order , update the quantity and return total price"""
        total_price = 0
        products_to_remove = []  #
        for product_index, quantity in shopping_list:
            product = self.product_list[product_index]
            total_price += product.buy(quantity)
            if product.quantity == 0:
                products_to_remove.append(product)

        for product in products_to_remove:
            self.remove_product(product)
        return total_price


    def get_all_products(self):
        """Gets all the active products"""
        active_product_list = []
        for product in self.product_list:
            if product.is_active():
                active_product_list.append(product)
        return active_product_list
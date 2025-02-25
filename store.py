import products

class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.quantity
        return total_quantity

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            total_price += (quantity * product.price)
        return float(total_price)

    def get_all_products(self):
        active_product_list = []
        for product in self.product_list:
            if product.active:
                active_product_list.append(product)
        return active_product_list










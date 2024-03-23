from abstract_category_order import AbstractCategoryOrder

class Order(AbstractCategoryOrder):
    """ Класс заказа """
def __init__(self, product, quantity):
    super().__init__(product, quantity)


def get_product(self):
    return self.product


def get_quantity(self):
    return self.quantity


def get_total_cost(self):
    return self.product * self.quantity

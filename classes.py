class Category:
    """ Класс категории, его атрибуты с описанием типов данных"""
    name = str
    description = str
    goods = list

    counting_the_number_of_unique_products = 0
    counting_the_number_of_categories = 0


    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.counting_the_number_of_categories += 1
        Category.counting_the_number_of_unique_products += 1




class Product:
    """ Класс продукты, его атрибуты с описанием типов данных"""
    name = str
    description = str
    price = float
    quantity_in_stock = int


    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock




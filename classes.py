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
        self.__goods = goods

        Category.counting_the_number_of_categories += 1
        Category.counting_the_number_of_unique_products += 1

    @property
    def goods(self):
        """Получение приватного атрибута __goods"""
        return self.__goods

    def add_goods(self, product):
        """Добавление данных приватного атрибута __goods"""
        self.__goods.append(product)

    @property
    def __str__(self):
        """Получение имени, цены и оставшегося количества"""
        current_list = []
        for product in self.__goods:
            current_list.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return current_list

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.__goods})'

    def __len__(self):
        self.counting_the_number_of_unique_products = len(self.__goods)
        return f'{self.name}, количество продуктов: {self.counting_the_number_of_unique_products} шт.'


class Product:
    """ Класс продукты, его атрибуты с описанием типов данных"""
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity

    @property
    def price(self):
        """Получение приватных данных через геттер"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Условия изменения цены"""
        if new_price <= 0:
            print('Цена введена некоректно')
        elif new_price < self.__price:
            user_answer = input('Цена понизилась. Установить эту цену? (y - да, n - нет)')
            if user_answer == 'y':
                self.__price = new_price
            else:
                print('Цена осталась прежней')
        else:
            self.__price = new_price

    def get_product_price(self):
        return self.price

    def __repr__(self):
        return f'Product({self.name}, {self.description}, {self.price}, {self.quantity})'

    @classmethod
    def add_new_product(cls, product_data, list_of_products=None):
        # забираем данные в переменные для удобства работы
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']

        if list_of_products:
            for product in list_of_products:
                if product.name == name:  # проверяем есть ли название нового товара в уже имеющихся
                    # если товар с похожим названием найден, объединяем количество устанавливаем наибольшую стоимость
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    return product

        new_product = cls(name, description, price, quantity)
        return new_product

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

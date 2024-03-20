class Category:
    """ Класс категории, его атрибуты с описанием типов данных"""
    name: str
    description: str
    goods: list

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

        """ошибка если объект не является классом Product или его наследником"""

        if not isinstance(product, Product):
            raise TypeError("Добавлять можно только объекты Product или его наследников")

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
    name: str
    description: str
    price: float
    quantity: int
    color = None

    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity
        self.color = color

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
    def add_new_product(cls, product_data: dict, list_of_products: list) -> object:
        # забираем данные в переменные для удобства работы
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']
        color = product_data['color']

        if list_of_products:
            for product in list_of_products:
                if product.name == name:  # проверяем есть ли название нового товара в уже имеющихся
                    # если товар с похожим названием найден, объединяем количество устанавливаем наибольшую стоимость
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    return product

        return cls(product['name'], product['description'], product['price'], product['quantity'], product['color'])

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


class Smartphone(Product):
    """Добавили класс смартфон с атрибутами производительность, модель, объем встроенной памяти, цвет."""
    productivity: int
    model: str
    built_in_memory_capacity: int

    def __init__(self, name, description, price, quantity, color, productivity, model, built_in_memory_capacity):
        super().__init__(name, description, price, quantity, color)

        self.productivity = productivity
        self.model = model
        self.built_in_memory_capacity = built_in_memory_capacity

    @classmethod
    def add_new_product(cls, product_data: dict) -> object:
        """Класс метод который принимает словарь и создает новый объект класса Product"""

        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"],
                   product_data["productivity"], product_data["model"], product_data["built_in_memory_capacity"],
                   product_data["color"])


class LawnGrass(Product):
    """Добавили класс трава газонная с доп. атрибутами страна-производитель, срок прорастания, цвет."""
    manufacturer_country: str
    germination_period: float

    def __init__(self, name, description, price, quantity, color, manufacturer_country, germination_period):
        super().__init__(name, description, price, quantity, color)

        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period

    @classmethod
    def add_new_product(cls, product_data):
        """Класс метод который принимает словарь и создает новый объект класса Product"""

        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"],
                   product_data["manufacturer_country"], product_data["germination_period"], product_data["color"])

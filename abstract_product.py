from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def get_product_price(self):
        """
        Функция для получения цены продукта
        """
        pass

    @abstractmethod
    def add_new_product(self, product, list_product):
        """
        Функция для инициализации нового объекта
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        Функция для отображения сжатой информации о продукте
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        Функция для отображения информации о количестве продукта
        """
        pass

    @abstractmethod
    def __add__(self, other):
        """
        Функция для отображения информации о сумме всех продуктов данной категории
        """
        pass
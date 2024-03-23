from abc import ABC, abstractmethod
class AbstractCategoryOrder(ABC):
    """ Абстрактный класс для категории и заказа """

    @abstractmethod
    def __str__(self):
        """
           Функция строкового отображения класса
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        Функция подсчета количество продуктов
        """
        pass

    @abstractmethod
    def goods(self):
        """
        Функция отображения продукта
        """
        pass
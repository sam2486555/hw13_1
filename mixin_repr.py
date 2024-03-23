class MixinRepr:

    def __init__(self, *args, **kwargs):
        """
        Выводит информацию какой объект был создан и его свойства
        """
        print(repr(self))

    def __repr__(self):
        """
        Выводит информацию о создании объекта, с названием класса и атрибутами
        :return:
        """
        return f'{self.__class__.__name__}({self.__dict__.items()})'
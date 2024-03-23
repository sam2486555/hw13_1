import pytest

from classes import Category, Product, Smartphone, LawnGrass

@pytest.fixture
def class_category():
    return Category("Шоколад Milca",
                    "Воздушный нежный вкус шоколада",
                    {
                        "name":"Milca пористый молочный",
                        "description":"молочный воздушный шоколад милка",
                        "price": 76.0,
                        "quantity": 75
                    })

def test_category_init(class_category):
    assert class_category.name == "Шоколад Milca"
    assert class_category.description == "Воздушный нежный вкус шоколада"
    assert class_category.goods == {
                        "name":"Milca пористый молочный",
                        "description":"молочный воздушный шоколад милка",
                        "price": 76.0,
                        "quantity": 75
                    }
    assert class_category.counting_the_number_of_categories == 1
    assert class_category.counting_the_number_of_unique_products == 1

def test_len_category(class_category):
    assert class_category.__len__() == 'Шоколад Milca, количество продуктов: 4 шт.'

@pytest.fixture
def class_product():
    return Product("Milca пористый молочный", "молочный воздушный шоколад милка", 76.0, 75, "молочный")

def test_product_init(class_product):
    assert class_product.name == "Milca пористый молочный"
    assert class_product.description == "молочный воздушный шоколад милка"
    assert class_product.price == 76.0
    assert class_product.quantity == 75
    assert class_product.color == "молочный"



def test_product_price(class_product):
    class_product.get_product_price()
    assert class_product.get_product_price() == 76.0

@pytest.fixture
def class_smartphone():
    return Smartphone("Samsung Galaxy",
        "Хорошая камера, топовые характеристики",
        180_000.0,
        5,
        "Space Gray",
        2500,
        "S23 Ultra",
        6)
def test_init_smartphone(class_smartphone):
    assert class_smartphone.name == "Samsung Galaxy"
    assert class_smartphone.description == "Хорошая камера, топовые характеристики"
    assert class_smartphone.price == 180_000.0
    assert class_smartphone.productivity == 2500
    assert class_smartphone.model == "S23 Ultra"
    assert class_smartphone.built_in_memory_capacity == 6
    assert class_smartphone.color == "Space Gray"

def test_creates_product_smartphone():
    assert Smartphone.add_new_product({
        "name": "Samsung Galaxy",
        "description": "Хорошая камера, топовые характеристики",
        "price": 180_000.0,
        "quantity": 5,
        "color": "Space Gray",
        "productivity": 2500,
        "model": "S23 Ultra",
        "built_in_memory_capacity": 6
    })

@pytest.fixture
def class_lawn_grass():
    return LawnGrass("Газон",
        "Густая красивая трава",
        150.0,
        200,
        "Зеленый цвет",
        "Китай",
        3.5
        )

def test_init_lawn_grass(class_lawn_grass):
    assert class_lawn_grass.name == "Газон"
    assert class_lawn_grass.description == "Густая красивая трава"
    assert class_lawn_grass.price == 150.0
    assert class_lawn_grass.manufacturer_country == "Китай"
    assert class_lawn_grass.germination_period == 3.5
    assert class_lawn_grass.color == "Зеленый цвет"

def test_creates_product_lawn_grass():
    assert LawnGrass.add_new_product({
        "name": "Газон",
        "description": "Густая красивая трава",
        "price": 150.0,
        "quantity": 200,
        "manufacturer_country": "Китай",
        "germination_period": 3.5,
        "color": "Зеленый цвет"
    })
import pytest

from classes import Category, Product

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
    assert class_category.counting_the_number_of_categories == 3
    assert class_category.counting_the_number_of_unique_products == 3

def test_get_name(class_category):
    class_category.get_name()
    assert class_category.get_name() == "Шоколад Milca"


def test_get_description(class_category):
    class_category.get_description()
    assert class_category.get_description() == "Воздушный нежный вкус шоколада"


def test_get_goods(class_category):
    class_category.get_goods()
    assert class_category.get_goods() == {
        "name":"Milca пористый молочный",
        "description":"молочный воздушный шоколад милка",
        "price": 76.0,
        "quantity": 75
    }

@pytest.fixture
def class_product():
    return Product("Milca пористый молочный", "молочный воздушный шоколад милка", 76.0, 75)

def test_product(class_product):
    assert class_product.name == "Milca пористый молочный"
    assert class_product.description == "молочный воздушный шоколад милка"
    assert class_product.price == 76.0
    assert class_product.quantity_in_stock == 75

def test_product_name(class_product):
    class_product.get_product_name()
    assert class_product.get_product_name() == "Milca пористый молочный"


def test_product_description(class_product):
    class_product.get_product_description()
    assert class_product.get_product_description() == "молочный воздушный шоколад милка"


def test_product_price(class_product):
    class_product.get_product_price()
    assert class_product.get_product_price() == 76.0


def test_product_quantity_in_stock(class_product):
    class_product.get_product_quantity_in_stock()
    assert class_product.get_product_quantity_in_stock() == 75

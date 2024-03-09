import pytest

import classes

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
    assert class_category.counting_the_number_of_categories == 1
    assert class_category.counting_the_number_of_unique_products == 1

# def test_goods(class_category):
#     class_category.goods()
#     assert class_category.goods() == {
#                         "name":"Milca пористый молочный",
#                         "description":"молочный воздушный шоколад милка",
#                         "price": 76.0,
#                         "quantity": 75
#                     }
#     assert type(class_category.goods()) == dict




# def test_get_product(class_category):
#
#     assert class_category == {
#         "name":"Milca пористый молочный",
#         "description":"молочный воздушный шоколад милка",
#         "price": 76.0,
#         "quantity": 75
#     }
@pytest.fixture
def class_product():
    return Product("Milca пористый молочный", "молочный воздушный шоколад милка", 76.0, 75)

def test_product(class_product):
    assert class_product.name == "Milca пористый молочный"
    assert class_product.description == "молочный воздушный шоколад милка"
    assert class_product.price == 76.0
    assert class_product.quantity_in_stock == 75


def test_product_price(class_product):
    class_product.get_product_price()
    assert class_product.get_product_price() == 76.0



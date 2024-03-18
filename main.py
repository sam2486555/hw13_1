import classes

"""тестовый список словарей продуктов"""

product_date = [
  {
    "name": "Шоколад Milca",
    "description": "Воздушный нежный вкус шоколада",
    "products": [
      {
        "name": "Milca пористый молочный",
        "description": "молочный воздушный шоколад милка",
        "price": 76.0,
        "quantity": 75,
        "color": "молочный"
      },
      {
        "name": "Milca пористый темный",
        "description": "темный воздушный шоколад милка",
        "price": 76.0,
        "quantity": 80,
        "color": "темный"
      },
      {
        "name": "Milca пористый белый",
        "description": "белый воздушный шоколад милка",
        "price": 73.0,
        "quantity": 70,
        "color": "белый"
      }
    ]
  },
  {
    "name": "Шоколад Nestle",
    "description": "Огромное разнообразие ваших любимых вкусов шоколада",
    "products": [
      {
        "name": "С арахисом",
        "description": "Шоколад со вкусом арахиса",
        "price": 56.0,
        "quantity": 123,
        "color": "молочный"
      },
      {
        "name": "С фундуком",
        "description": "Шоколад со вкусом фундука",
        "price": 55.0,
        "quantity": 113,
        "color": "молочный"
      },
      {
        "name": "С соленой карамелью",
        "description": "Шоколад со соленой карамели",
        "price": 57.0,
        "quantity": 117,
        "color": "молочный"
      }

    ]
  }
]


def convert_data(categories):
  """Получение списков с категориями и товарами"""
  convert_categories = []
  for category in categories:
    convert_products = []
    for product in category["products"]:
      current_product = classes.Product(product["name"],
                                        product["description"],
                                        product["price"],
                                        product["quantity"],
                                        product["color"])
      convert_products.append(current_product)
    current_category = classes.Category(category["name"],
                                        category["description"],
                                        convert_products)
    convert_categories.append(current_category)
  return convert_categories


for category in convert_data(product_date):
  print(f'Категория товара <<{category.name}>>')
  for product in category.goods:
    print(f'Товар - {product.name}')
    print(f'Количество на складе: {product.quantity_in_stock}')
    print(f'Цена товара: {product.price}')
    new_price = float(input('Укажите новую цену - '))
    product.price = new_price
    print(f'Новая цена: {product.price}')
    print(f'==================================================================')
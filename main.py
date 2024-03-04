from classes import Category, Product

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
        "quantity": 75
      },
      {
        "name": "Milca пористый темный",
        "description": "темный воздушный шоколад милка",
        "price": 76.0,
        "quantity": 80
      },
      {
        "name": "Milca пористый белый",
        "description": "белый воздушный шоколад милка",
        "price": 73.0,
        "quantity": 70
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
        "quantity": 123
      },
      {
        "name": "С фундуком",
        "description": "Шоколад со вкусом фундука",
        "price": 55.0,
        "quantity": 113
      },
      {
        "name": "С соленой карамелью",
        "description": "Шоколад со соленой карамели",
        "price": 57.0,
        "quantity": 117
      }

    ]
  }
]

"""создаем основную функцию"""
def main():


    list_category = []
    for prod in product_date:
      list_product = [un for un in prod["products"]]
      category = Category(prod["name"], prod["description"], prod["products"])
      list_category.append(f'{category.get_name()} '
                           f'{category.get_description()} '
                           f'{category.get_goods()} '
                           )
      result = []
      for element in list_product:
        product = Product(element["name"], element["description"],
                          element["price"], element["quantity"])
        result.append(f'{product.get_product_name()}'
                      f'{product.get_product_description()}'
                      f'{product.get_product_price()}'
                      f'{product.get_product_quantity_in_stock()}'
                      )
    return list_category

print(main())

if __name__ == '__main__':
    main()
from app import db
from app.database import Product

def create_product(name, price, quantity, description, category, unique_tag):
  db.session.add(
    Product(
      name=name,
      price=price,
      quantity=quantity,
      description=description,
      category=category,
      unique_tag=unique_tag
    )
  )
  db.session.commit()

if __name__ == "__main__":
  #
  create_product("Bananas", 10.00, 200, "Yummy Bananas from Mexico", "Produce", "AAA111")
  # create_product("Oranges", 12.00, 50)
  products = Product.query.all()
  print(products)
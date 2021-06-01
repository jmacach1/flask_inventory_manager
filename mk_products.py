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
  db.create_all()
  create_product("Banana Leaf Table", 700.00, 200, "Table in shape of Banana Leaf", "Furniture", "FURN111")
  create_product("Flower Chair", 200.00, 600, "Chairs shaped like flowers", "Furniture", "FURN222")
  create_product("Islander Sandals", 20.00, 300, "Thick sole sandals", "Footwear", "FOOT111")
  create_product("Coconut Wine", 30.00, 50, "Wine from Coconut", "Beverage", "BEVG111")
  # create_product("Oranges", 12.00, 50)
  products = Product.query.all()
  print(products)
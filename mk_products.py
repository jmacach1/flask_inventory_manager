from app import db
from app.database import Product, Review

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

def create_review(product_id, author, rating, review_text):
  db.session.add(
    Review(
      product_id=product_id,
      author=author,
      rating=rating,
      review_text=review_text
    )
  )
  db.session.commit()

if __name__ == "__main__":
  db.create_all()
  create_product("Banana Leaf Table", 700.00, 200, "Table in shape of Banana Leaf", "Furniture", "FURN111")
  create_product("Flower Chair", 200.00, 600, "Chairs shaped like flowers", "Furniture", "FURN222")
  create_product("Islander Sandals", 20.00, 300, "Thick sole sandals", "Footwear", "FOOT111")
  create_product("Coconut Wine", 30.00, 50, "Wine from Coconut", "Beverage", "BEVG111")
  products = Product.query.all()
  print(products)

  create_review(1, "Grover Cleveland", 4.5, "These tables are absolutely awesome, so cool." )
  create_review(2, "Howard Taft", 3.0, "Chairs look nice, not comforable though." )
  create_review(2, "Mary Lincoln", 4.5, "They were a sensation for dinner with close friends and family." )
  create_review(4, "US Grant", 4.5, "Fine wine, good for celebrating important occations" )
  reviews = Review.query.all()
  print(reviews)
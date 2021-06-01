# from app.database import Product

# if __name__ == "__main__":
#   products = Product.query.all()
#   for product in products:
#     print(product
    
from app import db

if __name__ == "__main__":
  db.drop_all()
from app import db 

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  price = db.Column(db.Float, nullable=False)
  quantity = db.Column(db.Integer, nullable=False)
  description = db.Column(db.Text, nullable=True)
  category = db.Column(db.String, nullable=True)
  unique_tag = db.Column(db.String, nullable=True, unique=True)
  active = db.Column(db.Boolean, nullable=False, default=True)

  def __repr__(self):
    return f"<Product id={self.id} name={self.name}>"
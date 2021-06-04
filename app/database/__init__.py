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
  reviews = db.relationship('Review', backref='product', lazy=True)

  def __repr__(self):
    return f"<Product id={self.id} name={self.name}>"

class Review(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  author = db.Column(db.String, nullable=False)
  rating = db.Column(db.Float, nullable=False)
  review_text = db.Column(db.Text, nullable=True)
  active = db.Column(db.Boolean, nullable=False, default=True)
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

  def __repr__(self):
    return f"<Review id={self.id} author={self.author} product={self.product_id}>"
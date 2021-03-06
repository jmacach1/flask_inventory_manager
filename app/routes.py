from flask import ( 
  render_template, 
  request,
  redirect,
  url_for,
  flash
  )
from app import app, db
from datetime import datetime
from app.database import Product, Review
from app.forms import ProductForm, ReviewForm

@app.route("/")
def index():
  version = {
    "ok" : True,
    "message" : "success",
    "version" : "1.0.0",
    "server_time" : datetime.now().strftime("%F %H:%M:%S")
  }
  return render_template("index.html", version=version)

# Read
@app.route("/products")
def get_products():
  products = Product.query.filter_by(active=True)
  return render_template("product_list.html", product_list=products)

@app.route("/products/<int:pid>")
def get_product_detail(pid):
  product = Product.query.filter_by(id=pid).first()
  reviews = Review.query.filter_by(product_id=pid)
  return render_template("product_detail.html", product=product, reviews=reviews)

# Create
@app.route("/products/registration")
def create_product_form():
  prod_form = ProductForm()
  return render_template("create_form.html", form=prod_form)

@app.route("/products", methods=["POST"])
def create_product():
    """Create a new product"""
    form = ProductForm(request.form)
    if form.validate():
        product = Product()
        product.name = form.name.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        product.description = form.description.data
        product.category = form.category.data
        product.unique_tag = form.unique_tag.data
        db.session.add(product)
        db.session.commit()
        flash(f"Product {product.name} created!")
        return redirect(url_for('get_products'))

    flash("Invalid data")
    return redirect(url_for('get_products'))

# update product
@app.route("/products/modifications/<int:pid>")
def update_product_form(pid):
  form = ProductForm()
  product = Product.query.filter_by(id=pid).first()
  return render_template("update_form.html", form=form, product=product)

@app.route("/products/<int:pid>", methods=["POST"])
def update_product(pid):
  form = ProductForm(request.form)
  if (form.validate()):
    product = Product.query.filter_by(id=pid).first()
    product.name = form.name.data
    product.price = form.price.data
    product.quantity = form.quantity.data
    product.description = form.description.data
    product.category = form.category.data
    product.unique_tag = form.unique_tag.data
    db.session.commit()
    flash(f"Product {product.name} Updated!")
    return redirect(url_for('get_products'))
    
  flash("Invalid Data!")
  return redirect(url_for('get_products'))

# Delete
@app.route("/products/delete/<int:pid>", methods=["POST"])
def delete_product(pid):
  product = Product.query.filter_by(id=pid).first()
  if product is None:
    flash(f"Product {pid} does not exist")
    return redirect(url_for('get_products'))

  product.active = False
  db.session.commit()
  flash(f"Product {product.name} Deleted!")
  return redirect(url_for('get_products'))
    
# Undo delete
@app.route("/products/deleted")
def get_deleted_products():
  products = Product.query.filter_by(active=False)
  return render_template("product_list_deleted.html", product_list=products)

@app.route("/products/undo_delete/<int:pid>", methods=["POST"])
def undo_delete_product(pid):
  product = Product.query.filter_by(id=pid).first()
  if product is None:
    flash(f"Product {pid} does not exist")
    return redirect(url_for('get_deleted_products'))

  product.active = True
  db.session.commit()
  flash(f"Product {product.name} Restored!")
  return redirect(url_for('get_deleted_products'))

  # Hard delete
@app.route("/products/hard_delete/<int:pid>", methods=["POST"])
def hard_delete_product(pid):
  product = Product.query.filter_by(id=pid).first()
  if product is None:
    flash(f"Product {pid} does not exist")
    return redirect(url_for('get_deleted_products'))

  db.session.delete(product)
  db.session.commit()
  flash(f"Product {product.name} deleted completely from Database!")
  return redirect(url_for('get_deleted_products'))


# Create Review
@app.route("/review/create_form/<int:pid>")
def create_review_form(pid):
  product = Product.query.filter_by(id=pid).first()
  review_form = ReviewForm()
  return render_template("create_review_form.html", form=review_form, product=product)

@app.route("/review/<int:pid>", methods=["POST"])
def create_review(pid):
    """Creating a review"""
    form = ReviewForm(request.form)

    product = Product.query.filter_by(id=pid).first()
    if product is None:
      flash(f"Product {pid} does not exist")
      return redirect(url_for('get_products'))
    if form.validate():
      review = Review()
      review.author = form.author.data
      review.rating = form.rating.data
      review.review_text = form.review_text.data
      review.product_id = form.product_id.data
      db.session.add(review)
      db.session.commit()
      flash(f"Review created!")
      return redirect(url_for('get_product_detail', pid=pid))

    flash("Invalid data")
    return redirect(url_for('get_product_detail', pid=pid))
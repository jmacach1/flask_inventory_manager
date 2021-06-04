from wtforms import (
  Form,
  StringField,
  FloatField,
  IntegerField,
  TextField,
  validators
)

class ProductForm(Form):
  style = {
    "style" : "width:100%"
  }
  name = StringField("Name", [validators.required(), validators.Length(min=4, max=45)], render_kw=style)
  price = FloatField("Price", [validators.required()], render_kw=style)
  quantity = IntegerField("Quantity", [validators.required()], render_kw=style)
  description = TextField("Description", [validators.required()], render_kw=style)
  category = StringField("category", [validators.required()], render_kw=style)
  unique_tag = StringField("unique_tag", [validators.required()], render_kw=style)


class ReviewForm(Form):
  style = {
    "style" : "width:100%"
  }
  author = StringField("Author", [validators.required(), validators.Length(min=2, max=45)], render_kw=style)
  rating = IntegerField("Rating", [validators.required()], render_kw=style)
  review_text = TextField("Text", [validators.required()], render_kw=style)
  product_id = IntegerField("Product_id", [validators.required()], render_kw=style)


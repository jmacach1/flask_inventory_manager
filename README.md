# Product Inventory Management

## URLs

### Read
"/" - project info
GET "/products" - returns a table of the products in inventory
GET "/products/<int:pid>" - return details for a product

### Create
GET "/products/registration" - returns html form for creating a product
POST "/products" - creates the product and persist into the database

### Update / Modify
GET "/products/modifications/<int:pid>" - html form to update product
POST "/products/<int:pid>" - updates the product

### Delete
GET "/products/deleted" - returns table of deleted products (active == False)

POST "/products/delete/<int:pid>" - soft delete on product, active field is set to value False

POST "/products/undo_delete/<int:pid>" - undo soft delete (restore) active field is set to value True

POST "/products/hard_delete/<int:pid>" - product is removed from database
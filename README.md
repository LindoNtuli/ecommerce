E-commerce Product API
## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>

This README provides documentation for the E-commerce API, designed for managing products and users in an online shopping platform. The API includes functionality for product management, user authentication, and searching/filtering products.

Table of Contents
1. Features
2. API Endpoints
- Create a New Product
- Retrieve a List of Products
- Retrieve Details of a Specific Product
- Update Product Details
- Delete a Product
- Search Products by Name or Description
- Retrieve Products by Category
3. Deployment
4. Pagination and Filtering

1. Features

Product Management (CRUD): Create, Read, Update, and Delete products with attributes such as Name, Description, Price, Category, Stock Quantity, Image URL, and Created Date.
User Management (CRUD): Create, Read, Update, and Delete users who manage products, ensuring authentication for these operations.
Product Search: Search for products by name or category with support for partial matches.
Product View: Retrieve a list of products or view individual details with filtering options.

2. API Endpoints
- Create a New Product
Endpoint
POST /api/products/

Request Parameters
Parameter	Type	Required	Description
name	string	Yes	The name of the product.
description	string	Yes	A detailed description of the product.
price	decimal	Yes	The price of the product.
stock	integer	Yes	The available stock quantity.
category_id	integer	No	The ID of the category the product belongs to.
Expected Response
Status: 201 Created

{
    "id": 1,
    "name": "Sample Product",
    "description": "This is a sample product.",
    "price": 10,
    "stock": 100,
    "category_id": 2
}
- Retrieve a List of Products
Endpoint
GET /api/products/

Request Parameters
Parameter	Type	Required	Description
page	integer	No	Page number for pagination (default is 1).
page_size	integer	No	Number of products per page (default is 10).
category_id	integer	No	Filter by category ID.
Expected Response
Status: 200 OK

{
    "count": 10,
    "next": "http://e-commerce.com/api/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Sample Product",
            "price": 10
        }
    ]
}
- Retrieve Details of a Specific Product
Endpoint
GET /api/products/{id}/

Request Parameters
Parameter	Type	Required	Description
id	integer	Yes	The ID of the product.
Expected Response
Status: 200 OK

{
    "id": 1,
    "name": "Sample Product",
    "description": "This is a sample product.",
    "price": 10,
    "stock": 100,
    "category_id": 2
}
- Update Product Details
Endpoint
PUT /api/products/{id}/

Request Parameters
Parameter	Type	Required	Description
id	integer	Yes	The ID of the product.
name	string	No	Updated name of the product.
description	string	No	Updated description of the product.
price	decimal	No	Updated price of the product.
stock	integer	No	Updated stock quantity.
category_id	integer	No	Updated category ID.
Expected Response
Status: 200 OK

{
    "id": 1,
    "name": "Updated Sample Product",
    "description": "This is an updated sample product.",
    "price": 30,
    "stock": 80,
    "category_id": 2
}
- Delete a Product
Endpoint
DELETE /api/products/{id}/

Request Parameters
Parameter	Type	Required	Description
id	integer	Yes	The ID of the product.
Expected Response
Status: 204 No Content

- Search Products by Name or Description
Endpoint

3. Deployment
- The API will be deployed on platforms like Heroku or PythonAnywhere. Ensure the deployed API is accessible, stable, and secure.
4. Pagination and Filtering
- Pagination is implemented on product listing and search endpoints to efficiently handle large datasets.
- Filtering options allow users to refine product searches based on categories, price ranges, and stock availability to enhance user experience.

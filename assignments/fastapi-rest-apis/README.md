# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice route creation, request validation, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Endpoints

#### Description
Set up a FastAPI app and implement simple `GET` routes so the server can return a welcome message and a health status response.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Add a `GET /` endpoint that returns a JSON welcome message
- Add a `GET /health` endpoint that returns a JSON status like `{"status": "ok"}`


### 🛠️ Add Product Data with Validation

#### Description
Create an in-memory product list and add endpoints to create and list products. Use Pydantic models to validate incoming request data.

#### Requirements
Completed program should:

- Define a Pydantic model for product input (`name`, `price`, and `in_stock`)
- Add a `POST /products` endpoint that validates and stores a new product
- Add a `GET /products` endpoint that returns all saved products
- Return meaningful JSON responses for successful requests


### 🛠️ Implement Update and Delete Operations

#### Description
Complete the API by adding `PUT` and `DELETE` endpoints to modify and remove products by ID.

#### Requirements
Completed program should:

- Add a `PUT /products/{product_id}` endpoint that updates an existing product
- Add a `DELETE /products/{product_id}` endpoint that removes a product
- Return a `404` response when a product ID is not found
- Demonstrate all CRUD endpoints using sample requests in comments or a short test section

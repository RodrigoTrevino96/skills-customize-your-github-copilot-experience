from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Products API")


class ProductInput(BaseModel):
    name: str
    price: float
    in_stock: bool


products = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Products API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/products")
def list_products():
    return products


@app.post("/products")
def create_product(product: ProductInput):
    product_data = product.model_dump()
    product_data["id"] = len(products) + 1
    products.append(product_data)
    return product_data


@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductInput):
    for index, existing in enumerate(products):
        if existing["id"] == product_id:
            updated = product.model_dump()
            updated["id"] = product_id
            products[index] = updated
            return updated

    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, existing in enumerate(products):
        if existing["id"] == product_id:
            removed = products.pop(index)
            return {"deleted": removed}

    raise HTTPException(status_code=404, detail="Product not found")

from fastapi import FastAPI, APIRouter, Query
from models.schemes import *
app = FastAPI(title = "Mis productos")

api_router = APIRouter()

products = [
    {
        "id": 1,
        "name": "Iphone 13",
        "quantity": 12,
        "description": "nuevo celular de apple",
        "precio": 4500000,
        "category": 1
    },

    {
        "id": 2,
        "name": "MSI GF13 thin",
        "quantity": 10,
        "description": "laptop para gamer",
        "precio": 5000000,
        "category": 2

    }

]

@api_router.get("/products/")
def product_list() -> dict:
    return products

@api_router.get("/products/{product_id}")
def fetch_product(*, product_id: int)-> dict:
    result = [product for product in products if product["id"]==product_id]
    if result:
        return result[0]


@api_router.get("/products/search/")
def search_products_by_category(*, category: int = Query(...)) -> dict:
    results = filter(lambda product: category == product["category"], products)
    return list(results)


@api_router.post("/products/", status_code = 201, response_model = Product)
def create_product(*, product_in: ProductCreate) -> dict:
	new_entry_id = len(products)+1
	product_entry = Product(
		id = new_entry_id,
		name = product_in.name,
		quantity = product_in.quantity,
		description = product_in.description,
        precio = product_in.precio,
		category = product_in.category
	)
	products.append(product_entry.dict())
	return product_entry

app.include_router(api_router)
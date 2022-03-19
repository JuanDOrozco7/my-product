from pydantic import BaseModel




class Product(BaseModel):
    id: int
    name: str
    quantity: int
    description: str
    precio: int
    category: int

class ProductCreate(BaseModel):
    name: str
    quantity: int
    description: str
    precio: int
    category: int
from pydantic import BaseModel

class ProductModel(BaseModel):
    name: str
    amount_L: str
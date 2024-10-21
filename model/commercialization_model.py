from pydantic import BaseModel


class CommercializationModel(BaseModel):
    country: str
    amount_KG: str
    value_dolar: str
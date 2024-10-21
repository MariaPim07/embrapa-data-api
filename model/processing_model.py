from pydantic import BaseModel

class ProcessingModel(BaseModel):
    name: str
    amount_KG: str
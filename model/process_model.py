from model.product_model import Product

class Process:
    def __init__(self, product: Product, amount_L: float, amount_Kg: float, process: str,
                 country: str, classification: str):
        self._product = product
        self._amount_L = amount_L
        self._amount_Kg = amount_Kg
        self._process = process
        self._country = country
        self._classification = classification

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product

    @property
    def amount_L(self):
        return self._amount_L

    @amount_L.setter
    def amount_L(self, amount_L: float):
        self._amount_L = amount_L

    @property
    def amount_Kg(self):
        return self._amount_Kg

    @amount_Kg.setter
    def amount_Kg(self, amount_Kg: float):
        self._amount_Kg = amount_Kg

    @property
    def process(self):
        return self._process

    @process.setter
    def process(self, process: str):
        self._process = process

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country: str):
        self._country = country

    @property
    def classification(self):
        return self._classification

    @classification.setter
    def classification(self, classification: str):
        self._classification = classification

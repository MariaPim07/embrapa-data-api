class Product:
    def __init__(self, product_name: str, product_category: str):
        self._product_name = product_name
        self._product_category = product_category

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, product_name: str):
        self._product_name = product_name

    @property
    def product_category(self):
        return self._product_name

    @product_category.setter
    def set_product_category(self, product_category: str):
        self._product_category = product_category
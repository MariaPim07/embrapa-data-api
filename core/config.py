import os

class Settings:
    BASE_URL: str = os.getenv("BASE_URL", "http://vitibrasil.cnpuv.embrapa.br/index.php")

settings = Settings()
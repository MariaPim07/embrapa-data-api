from fastapi import APIRouter, Query

from core.option_enum import Option, Option_Ex
from model.commercialization_model import CommercializationModel
from model.processing_model import ProcessingModel
from model.product_model import ProductModel
from services.commercialization_service import CommercializationService
from services.embrapa_service import EmbrapaService
from services.processing_service import ProcessingService
from services.product_service import ProductService

router = APIRouter()

product_service = ProductService()
processing_service = ProcessingService()
commercialization_service = CommercializationService()

embrapa_service = EmbrapaService()

@router.get("/production")
def get_production(year: str = Query(None, description="Ano.")) -> list[ProductModel]:
    """
        Endpoint used to return wine production data,
        juices and derivatives from Rio Grande do Sul.
    """
    try:
        return product_service.get_production(year=year)
    except Exception:
        raise Exception


@router.get("/processing")
def get_processing(year: str = Query(None, description="Ano."),
                   option: Option = Query(Option.OPTION_1.value,
                                          description="Subopção: Viníferas, Americanas e Híbridas, "
                                                            "Uvas de Mesa, Sem Classificação.")) -> list[ProcessingModel]:
    """
        Endpoint used to return data from
        quantity of grapes processed in Rio Grande do Sul.
    """
    try:
        return processing_service.get_processing(year=year, option=option.value)
    except Exception:
        raise Exception


@router.get("/commercialization")
def get_commercialization(year: str = Query(None, description="Ano.")) -> list[ProductModel]:
    """
        Endpoint used to return data from
        marketing of wines and derivatives in Rio Grande do Sul.
    """
    try:
        return product_service.get_commercialization(year=year)
    except Exception:
        raise Exception

@router.get("/importation")
def get_importation(year: str = Query(None, description="Ano."),
                    option: Option = Query(Option.OPTION_1.value,
                    description="Subopção: Vinhos de Mesa, Espumantes, "
                    "Uvas Frescas, Uvas Passas, Suco de Uva.")) -> list[CommercializationModel]:
    """
        Endpoint used to return grape derivatives import data.
    """
    try:
       return commercialization_service.get_importation(year=year, option=option.value)
    except Exception:
        raise Exception


@router.get("/exportation")
def get_exportation(year: str = Query(None, description="Ano."),
                    option: Option_Ex = Query(Option_Ex.OPTION_1.value,
                    description="Subopção: Vinhos de Mesa, Espumantes, "
                    "Uvas Frescas, Uvas Passas, Suco de Uva.")) -> list[CommercializationModel]:
    """
        Endpoint used to return grape derivatives export data.
    """
    try:
        return commercialization_service.get_exportation(year=year, option=option.value)
    except Exception:
        raise Exception

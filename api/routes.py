from fastapi import APIRouter
from services.embrapa_service import Embrapa
from core.option_enum import Option

router = APIRouter()

embrapa = Embrapa()

@router.get("/production")
def get_production(year):
   return Embrapa.find_data(embrapa, year, 'opcao=opt_02')

@router.get("/processing")
def get_processing(year, option):
    return Embrapa.find_data(embrapa, year, f'{Option[str(option)].value}&opcao=opt_03')

@router.get("/commercialization")
def get_commercialization(year):
    return Embrapa.find_data(embrapa, year, 'opcao=opt_04')

@router.get("/importation")
def get_importation(year, option):
    return Embrapa.find_data(embrapa, year, f'{Option[str(option)].value}&opcao=opt_05')

@router.get("/exportation")
def get_exportation(year, option):
    return Embrapa.find_data(embrapa, year, f'{Option[str(option)].value}&opcao=opt_06')
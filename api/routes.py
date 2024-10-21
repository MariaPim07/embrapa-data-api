from fastapi import APIRouter
from services.embrapa_service import Embrapa
from core.option_enum import Option

router = APIRouter()

embrapa = Embrapa()

@router.get("/production/")
def getProduction(year):
   return Embrapa.findData(embrapa, year, 'opcao=opt_02')

@router.get("/processing/")
def getProcessing(year, option):
    return Embrapa.findData(embrapa, year, f'{Option[str(option)].value}&opcao=opt_03', 1)

@router.get("/commercialization/")
def getCommercialization(year):
    return Embrapa.findData(embrapa, year, 'opcao=opt_04')

@router.get("/importation/")
def getImportation(year, option):
    return Embrapa.findData(embrapa, year, f'{Option[str(option)].value}&opcao=opt_05', 2)

@router.get("/exportation/")
def getExportation(year, option):
    return Embrapa.findData(embrapa, year, f'{Option[str(option)].value}&opcao=opt_06', 2)
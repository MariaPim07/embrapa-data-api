from fastapi import HTTPException

from core.option_enum import Option
from model.processing_model import ProcessingModel
from services.embrapa_service import EmbrapaService

class ProcessingService:
    def __init__(self):
        self.embrapa_service = EmbrapaService()
        return

    def get_processing(self, year: str, option: str) -> list[ProcessingModel]:
        try:
            processing_model_list: list[ProcessingModel] = []

            if option == Option.OPTION_4.value:
                for processing in self.embrapa_service.find_data(year=year, endpoint=f'subopcao={str(option)}&opcao=opt_03'):
                    processing_model_list.append(ProcessingModel(name=processing["Sem definição"],
                                                                 amount_KG=processing["Quantidade (Kg)"]))
            else:
                for processing in self.embrapa_service.find_data(year=year, endpoint=f'subopcao={str(option)}&opcao=opt_03'):
                    processing_model_list.append(ProcessingModel(name=processing["Cultivar"],
                                                                 amount_KG=processing["Quantidade (Kg)"]))

            return processing_model_list
        except HTTPException as err:
            raise HTTPException(err.status_code, err.detail)
        except Exception:
            raise Exception

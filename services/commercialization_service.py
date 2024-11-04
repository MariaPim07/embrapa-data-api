from model.commercialization_model import CommercializationModel
from services.embrapa_service import EmbrapaService

class CommercializationService:
    def __init__(self):
        self.embrapa_service = EmbrapaService()
        return

    def get_importation(self, year: str, option: str) -> list[CommercializationModel]:
        commercialization_model_list: list[CommercializationModel] = []

        for commercialization in self.embrapa_service.find_data(year=year, endpoint=f'subopcao={str(option)}&opcao=opt_05'):
            commercialization_model_list.append(CommercializationModel(country=commercialization["Países"],
                                                                       amount_KG=commercialization["Quantidade (Kg)"],
                                                                       value_dolar=commercialization["Valor (US$)"]))
        return commercialization_model_list

    def get_exportation(self, year: str, option: str) -> list[CommercializationModel]:
        commercialization_model_list: list[CommercializationModel] = []

        for commercialization in self.embrapa_service.find_data(year=year, endpoint=f'subopcao={str(option)}&opcao=opt_06'):
            commercialization_model_list.append(CommercializationModel(country=commercialization["Países"],
                                                                       amount_KG=commercialization["Quantidade (Kg)"],
                                                                       value_dolar=commercialization["Valor (US$)"]))
        return commercialization_model_list

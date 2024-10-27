from bs4 import BeautifulSoup
import requests
from core.settings import settings

class Embrapa:
    def __init__(self):
        return

    def find_data(self, year, endpoint):
        try:
            url = f"{settings.BASE_URL}?ano={year}&{endpoint}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            table = soup.find("table", {'class':'tb_base tb_dados'})
            headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]

            # TODO: alterar retorno.
            result = self.__group_data(headers, table)

            return result
        except Exception as error:
            print(error)
            return Exception("Ocorreu um erro ao realizar o request.")


    def __group_data(self, headers, table):
        result = []

        for row in table.find("tbody").find_all("tr"):
            cells = row.find_all("td")
            item = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}

            result.append(item)

        return result

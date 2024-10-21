from bs4 import BeautifulSoup
import requests
from fastapi import HTTPException

from core.settings import settings

class EmbrapaService:
    def __init__(self):
        return

    def find_data(self, year, endpoint):
        try:
            url = f"{settings.BASE_URL}?ano={year}&{endpoint}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            table = soup.find("table", {'class':'tb_base tb_dados'})
            headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]

            # TODO: alterar retorno (mapeado /model).
            result = self.__group_data(headers, table)

            return result
        except:
            raise HTTPException(500, "An error occurred while making the request to Empraba.")


    def __group_data(self, headers, table):
        try:
            result = []

            for row in table.find("tbody").find_all("tr"):
                cells = row.find_all("td")
                item = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}

                result.append(item)

            return result
        except:
            raise HTTPException(500, "An error occurred while grouping the data.")
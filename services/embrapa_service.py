import os
from bs4 import BeautifulSoup
import requests

class Embrapa:
    def __init__(self):
        return

    def findData(self, year, endpoint, endpointType):
        try:
            url = f"{os.getenv("BASE_URL")}?ano={year}&{endpoint}"

            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("table", {'class':'tb_base tb_dados'})

            return self.__formatData(table, endpointType)
        except error:
            print(error)
            return Exception("Ocorreu um erro ao realizar o request.")

    def __formatData(self, table, endpointType):
        data = []

        if endpointType == 1:
            for row in table.find("tbody").find_all("tr"):
                cells = row.find_all("td")
                total = len(cells)
                for i in range(len(cells)):
                    if i < total - 1:
                        data.append({f"{cells[i].get_text(strip=True)}": cells[i + 1].get_text(strip=True)})
        else:
            for row in table.find("tbody").find_all("tr"):
                cells = row.find_all("td")
                total = len(cells)
                for i in range(len(cells)):
                    if i < total - 2:
                        data.append({"country": cells[i].get_text(strip=True),
                                     "amount": cells[i + 1].get_text(strip=True),
                                     "value": cells[i + 2].get_text(strip=True)})
        #
        # tfoot = table.find("tfoot", class_="tb_total")
        # if tfoot:
        #     total_cells = tfoot.find_all("td")
        #     if len(total_cells) == len(headers):
        #         total = {headers[i]: total_cells[i].get_text(strip=True) for i in range(len(headers))}

        return data

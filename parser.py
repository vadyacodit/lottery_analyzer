import requests
import typing


from fake_useragent import FakeUserAgent
from typing import *


class Parser:
    def __init__(self, source_url: str, init_date: str, final_date: str) -> None:
        self.headers = {'user_agent': FakeUserAgent().random}
        self.source_url = source_url
        self.init_date = init_date
        self.final_date = final_date



    def parse_data(self) -> Dict:

        params = {
            'game_id': 'BONO',
            'celebrados': 'true',
            'fechaInicioInclusiva': {self.init_date},
            'fechaFinInclusiva': {self.final_date},
        }

        response = requests.get(
            'https://www.loteriasyapuestas.es/servicios/buscadorSorteos',
            params=params,
            headers=self.headers,
        )
        result_json = response.json()
        result_dict = {}
        for result in result_json:
            numbers = [num.strip() for num in result['combinacion'].split('-')][:5]
            result_dict[result['fecha_sorteo'][:10]] = numbers

        return result_dict




import requests
import re

from typing import *
from fake_useragent import FakeUserAgent


def parse_data(url, init_date, final_date) -> Dict:
    headers = {
        'user-agent': FakeUserAgent().random,
    }

    params = {
        'game_id': 'BONO',
        'celebrados': 'true',
        'fechaInicioInclusiva': init_date,
        'fechaFinInclusiva': final_date,
    }

    response = requests.get(
        'https://www.loteriasyapuestas.es/servicios/buscadorSorteos',
        params=params,
        headers=headers,
    )

    result_json = response.json()
    result_dict = {}
    for result in result_json:
        numbers = re.findall(r'\d{2}', result['combinacion'].split(' C(')[0])
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        result_dict[result['fecha_sorteo'][:10]] = numbers

    return result_dict


def create_matrix(result_dict: Dict) -> List:
    matrix = []
    for val in result_dict.values():
        matrix.append(val)
    return matrix


link = 'https://www.loteriasyapuestas.es/es/resultados/bonoloto'
parsed_data = parse_data(url=link, init_date='20240815', final_date='20240915')
print(parsed_data)

print(create_matrix(parsed_data))

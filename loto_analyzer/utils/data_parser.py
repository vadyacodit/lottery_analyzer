import requests
import re

from typing import *
from fake_useragent import FakeUserAgent

def get_data(url, init_date, final_date) -> Dict:
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
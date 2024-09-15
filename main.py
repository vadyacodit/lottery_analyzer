from parser import Parser

link = 'https://www.loteriasyapuestas.es/es/resultados/bonoloto'
parser = Parser(source_url=link, init_date='20240815', final_date='20240915')

parsed_data = parser.parse_data()
print(parsed_data)
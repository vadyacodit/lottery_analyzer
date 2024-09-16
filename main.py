from loto_analyzer.loto import Loto


link = 'https://www.loteriasyapuestas.es/es/resultados/bonoloto'
init_date = '20240815'
final_date = '20240915'

loto = Loto(link, init_date, final_date)
loto.prettify_matrix()






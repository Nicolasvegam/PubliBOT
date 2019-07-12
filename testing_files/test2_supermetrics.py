import requests
import json

#Integración con Ad Manager
#Para obtener la data ingresar a
# https://supermetrics.com/tools/ y solicitar la tabla correspondiente
Ad_Manager = "\n    Análisis de datos desde Ad Manager    \n"
print(Ad_Manager)
# Realiza la consulta GET en la página
r = requests.get('https://supermetrics.com/api/v1/getData?metrics=TOTAL_INVENTORY_LEVEL_CTR_perc%2CTOTAL_INVENTORY_LEVEL_CLICKS&dimensions=ADVERTISER_NAME&maxResults=1000&dateRangeType=custom&start-date=2019-05-27&end-date=2019-06-07&profiles=%5B%7B%22ID%22%3A%22105773011%22%2C%22name%22%3A%22Mercado%20Libre%22%7D%5D&otherParams=%5B%5D&dataSource=DFP&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG')


# Obtener texto
#print(r.text)
text = json.loads(r.text)

for element in text["data"]:
    print(element)

# Integración con Google Analytics
Analytics = "\n    Análisis de datos desde Google Analytics    \n"
print(Ad_Manager)
# Realiza la consulta GET en la página
t = requests.get('https://supermetrics.com/api/v1/getData?metrics=organicsearches&dimensions=dayOfWeekWithName&maxResults=5000&dateRangeType=custom&start-date=2019-05-27&end-date=2019-06-07&profiles=%5B%7B%22ID%22%3A%22112132896%22%2C%22name%22%3A%22Applications%20Chile%3A%20Unfiltered%20-%20apps.mercadolibre.cl%22%7D%5D&otherParams=%5B%5D&dataSource=GA&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG')

# Obtener texto
#print(t.text)
text_analytics = json.loads(t.text)

for element in text_analytics["data"]:
    print(element)

import requests
import json

#Integración con Ad Manager/Google Analytics
#Para obtener la data ingresar a
# https://supermetrics.com/tools/ y solicitar la tabla correspondiente

class Integration:

    def get_data(self, query):

        text = requests.get(query)
        data = json.loads(text.text)

        return data

    def filter_data(self, data, seller):

        selected_data = []

        for element in data["data"]:
            if seller in element[0]:
                selected_data.append(element)

        return selected_data


seller = "Somela"
admanager_query = 'https://supermetrics.com/api/v1/getData?metrics=TOTAL_INVENTORY_LEVEL_CLICKS%2CTOTAL_INVENTORY_LEVEL_CTR_perc%2CTOTAL_INVENTORY_LEVEL_IMPRESSIONS&dimensions=LINE_ITEM_NAME&filters=ORDER_NAME%3D%40MLC%3BORDER_NAME%3D%40somela&maxResults=1000&dateRangeType=thisyear&profiles=%5B%7B%22ID%22%3A%22105773011%22%2C%22name%22%3A%22Mercado%20Libre%22%7D%5D&otherParams=%5B%5D&dataSource=DFP&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG'.format(seller)

analytics_type_user = 'https://supermetrics.com/api/v1/getData?metrics=pageviews%2Cuniquepageviews&dimensions=PagePath%2CVisitorType&filters=PagePath%3D%40{0}&maxResults=1000&dateRangeType=custom&start-date=2019-06-01&end-date=2019-06-30&profiles=%5B%7B%22ID%22%3A%2279575411%22%2C%22name%22%3A%22MercadoLibre%20Chile%3A%20Unfiltered%20-%20mercadolibre.cl%22%7D%5D&otherParams=%5B%5D&dataSource=GA&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG'.format(seller)

analytics_region = 'https://supermetrics.com/api/v1/getData?metrics=pageviews2&dimensions=PagePath%2CRegion&filters=PagePath%3D~{0}&maxResults=1000&dateRangeType=custom&start-date=2019-06-01&end-date=2019-06-30&profiles=%5B%7B%22ID%22%3A%2279575411%22%2C%22name%22%3A%22MercadoLibre%20Chile%3A%20Unfiltered%20-%20mercadolibre.cl%22%7D%5D&otherParams=%5B%5D&dataSource=GA&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG'.format(seller)

analytics_day = 'https://supermetrics.com/api/v1/getData?metrics=pageviews2&dimensions=PagePath%2CdayOfWeekWithName&filters=PagePath%3D%40{0}&maxResults=1000&dateRangeType=custom&start-date=2019-06-01&end-date=2019-06-30&profiles=%5B%7B%22ID%22%3A%2279575411%22%2C%22name%22%3A%22MercadoLibre%20Chile%3A%20Unfiltered%20-%20mercadolibre.cl%22%7D%5D&otherParams=%5B%5D&dataSource=GA&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG'.format(seller)


if __name__ == '__main__':
    class_ = Integration()
    data = class_.get_data(admanager_query)
    data_1 = class_.get_data(analytics_type_user)
    data_2 = class_.get_data(analytics_region)
    data_3 = class_.get_data(analytics_day)

    for element in data["data"]:
        print(element)
    for element in data_1["data"]:
        print(element)
    for element in data_2["data"]:
        print(element)
    for element in data_3["data"]:
        print(element)
    
    #

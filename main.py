from Supermetrics_API import Integration
from Tableau_API import Tableau_extractor
from Design import PowerPointer
#from cropping import cropping_images
import time


all = {
'SACTI': ['FENSA', 'MADEMSA', 'ELECTROLUX'],
'SOMELASA': ['SOMELA', 'ELECTROLUX'],
'SERVICIOALCLIENTE001':	['SONY'],
'IROBOT.CORP': ['IROBOT'],
'CITROENCHILESAC': ['CITROEN'],
'ONLINECLUB.TO': ['PAMPERS','PG','BLACK DECKER','REMINGTON','NAUTIKA'], #BLACK DECKER ad Manager, nautika no tiene
'SCOTIABANK CHILE':	['SCOTIABANK'], #no hay tableau
'ROICHEN': ['ROICHEN'],
'MOBILEHUT': ['MOTOROLA','MOBILE HUT'],
'CHILEMATCOMSPA': ['CHILEMAT'],
'ESTURIOTIENDAOFICIAL':	['RAYBAN'],
'COMPANIAS CIC': ['CIC'],
'DOITE OUTDOOR': ['DOITE'],
'RADIOVICTORIA1':[ 'RCA','TCL'],
'SAMSUNG_CL': ['SAMSUNG'],
'SALIPPI':	['LIPPI'],
'TC-TIENDA-CL':	['PHILIPS'],
'COMERCIAL KALTEMP': ['KALTEMP'],
'TIENDA_O':	['EVERLAST'],
'ENTELPCSCOMUNICACIONESS':	['ENTEL'],
'LOREAL.ONLINECLUB': ['LOREAL'],
'OVIEDO': ['OVIEDO'], #FERRETERIA OVIEDO
'INDUSTRIASCELTALIMITADA':	['CELTA'],
'ROBERTBOSCHSA':	['JUNKERS','BOSCH'], #junkers in ad manager, bosch in ad manager
'HBRIONESCOMERCIALSA':	['SWATCH','GUESS','FESTINA'],
'ECOMSUR OFICIAL': ['STANLEY',  'BLACK DECKER', 'DEWALT'],
'REBAJAS_GAMA':	['GAMA'],
'CASAMARILLA1920':	['CASA AMARILLA']
}

def Robot(Tableau_Store, seller, start_date, end_date, pr):

    #Supermetrics Queries
    admanager_query = 'https://supermetrics.com/api/v1/getData?metrics=TOTAL_INVENTORY_LEVEL_IMPRESSIONS%2CTOTAL_INVENTORY_LEVEL_CLICKS%2CTOTAL_INVENTORY_LEVEL_CTR_perc&dimensions=LINE_ITEM_NAME&filters=LINE_ITEM_NAME%3D%40MLC%3BLINE_ITEM_NAME%3D%40{0}&maxResults=1000&dateRangeType=custom&start-date={1}&end-date={2}&profiles=%5B%7B%22ID%22%3A%22105773011%22%2C%22name%22%3A%22Mercado%20Libre%22%7D%5D&otherParams=%5B%5D&dataSource=DFP&dsUser=blas.herrera%40mercadolibre.com&apiKey=api_9UTfgv7U9uv2W6kKPNuBWwkjqFDT31ghsvgZKBn9CZerBENbtA7dr1Heg73wn6vCl5F97lqpJOI3Glw7xQmiPd3ZW4pntaQjrIVc'.format(seller, start_date, end_date)

    #admanager_query = 'https://supermetrics.com/api/v1/getData?metrics=TOTAL_INVENTORY_LEVEL_IMPRESSIONS%2CTOTAL_INVENTORY_LEVEL_CLICKS%2CTOTAL_INVENTORY_LEVEL_CTR_perc&dimensions=LINE_ITEM_NAME&filters=LINE_ITEM_NAME%3D%40MLC%3BLINE_ITEM_NAME%3D%40{0}&maxResults=1000&dateRangeType=custom&start-date={1}&end-   ##date={2}&profiles=%5B%7B%22ID%22%3A%22105773011%22%2C%22name%22%3A%22Mercado%20Libre%22%7D%5D&otherParams=%5B%5D&dataSource=DFP&dsUser=blas.herrera%40mercadolibre.com&apiKey=api_9UTfgv7U9uv2W6kKPNuBWwkjqFDT31ghsvgZKBn9CZerBENbtA7dr1Heg73wn6vCl5F97lqpJOI3Glw7xQmiPd3ZW4pntaQjrIVc'.format(seller, start_date, end_date)

    #analytics_type_user = 'https://supermetrics.com/api/v1/getData?metrics=pageviews&dimensions=VisitorType&filters=PagePath%3D%40{0}&maxResults=1000&dateRangeType=custom&start-date={1}&end-date={2}&profiles=%5B%7B%22ID%22%3A%2279575411%22%2C%22name%22%3A%22MercadoLibre%20Chile%3A%20Unfiltered%20-#%20mercadolibre.cl%22%7D%5D&otherParams=%5B%5D&dataSource=GA&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG'.format(seller, start_date, end_date)

    #analytics_region = 'https://supermetrics.com/api/v1/getData?metrics=pageviews2&dimensions=PagePath%2CRegion&filters=PagePath%3D~{0}&maxResults=1000&dateRangeType=custom&start-date={1}&end-date={2}&profiles=%5B%7B%22ID%22%3A%2279575411%22%2C%22name%22%3A%22MercadoLibre%20Chile%3A%20Unfiltered%20-#%20mercadolibre.cl%22%7D%5D&otherParams=%5B%5D&dataSource=GA&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG'.format(seller, start_date, end_date)

    #analytics_day = 'https://supermetrics.com/api/v1/getData?metrics=pageviews&dimensions=dayOfWeekWithName&filters=PagePath%3D%40{0}&maxResults=1000&dateRangeType=custom&start-date={1}&end-date={2}&profiles=%5B%7B%22ID%22%3A%2279575411%22%2C%22name%22%3A%22MercadoLibre%20Chile%3A%20Unfiltered%20-#%20mercadolibre.cl%22%7D%5D&otherParams=%5B%5D&dataSource=GA&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG'.format(seller, start_date, end_date)

    #analytics_age = 'https://supermetrics.com/api/v1/getData?metrics=pageviews&dimensions=visitorAgeBracket&filters=PagePath%3D%40scotiabank&maxResults=1000&dateRangeType=custom&start-date=2019-01-02&end-date=2019-07-03&profiles=%5B%7B%22ID%22%3A%2279575411%22%2C%22name%22%3A%22MercadoLibre%20Chile%3A%20Unfiltered%20-#%20mercadolibre.cl%22%7D%5D&otherParams=%5B%5D&dataSource=GA&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG'

    #analytics_sex = 'https://supermetrics.com/api/v1/getData?metrics=pageviews&dimensions=visitorGender&filters=PagePath%3D%40{0}&maxResults=1000&dateRangeType=custom&start-date={1}&end-date={2}&profiles=%5B%7B%22ID%22%3A%2279575411%22%2C%22name%22%3A%22MercadoLibre%20Chile%3A%20Unfiltered%20-#%20mercadolibre.cl%22%7D%5D&otherParams=%5B%5D&dataSource=GA&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG'.format(seller, start_date, end_date)

    #analytics_devices = 'https://supermetrics.com/api/v1/getData?metrics=pageviews&dimensions=mobileDeviceBranding&filters=PagePath%3D%40{0}&maxResults=1000&dateRangeType=custom&start-date={1}&end-date={2}&profiles=%5B%7B%22ID%22%3A%2279575411%22%2C%22name%22%3A%22MercadoLibre%20Chile%3A%20Unfiltered%20-#%20mercadolibre.cl%22%7D%5D&otherParams=%5B%5D&dataSource=GA&dsUser=ext_nicovega%40mercadolibre.com&apiKey=api_g29hM3MCYvfUeQcaTBm8nXfi4PZXN5VsySTzJfUtICgo0ogcNC4ljb5A7ECHwubTLdGw6bgKR7j3cge0pAbn09PWZTDdLKtGihVG'.format(seller, start_date, end_date)

    #Getting data from Supermetrics Queries

    class_ = Integration()
    data = class_.get_data(admanager_query)

    print("{0}: {1}", seller,data)

    if data["notes"]["status"] == 'success':
        print("Creando tabla para {0}\n".format(seller))
        ad_manager = data["data"]
        pr.add_table(ad_manager, 'Advertising Performance', 3)

    pr.save('test_{0}'.format(seller))

if __name__ == '__main__':

    start_date = '2019-07-01' # 2019-06-01 format año/mes/dia
    end_date =  '2019-07-09' # 2019-06-01 format año/mes/dia

    print("Opciones: ")
    for tienda_madre in all:
        print("Filtro Tableau: {0} - Filtro Ad Manager {1} ".format(tienda_madre, all[tienda_madre]))

    tableau = input("\nFiltro Tableau: ")
    ad_manager_seller = input("\nFiltro AdManager: ")

    #start_date = input("\nIngrese fecha de inicio (formato año-mes-días ej: {0}): ".format(start_date))
    #end_date = input("\nIngrese fecha de término (formato año-mes-días ej: {0}): ".format(end_date))
    start_date = '2019-07-01' # 2019-06-01 format año/mes/dia
    end_date =  '2019-07-09' # 2019-06-01 format año/mes/dia

    #cropping_images()

    pr = PowerPointer()
    pr.first_slide()
    class_ = Tableau_extractor()
    class_.get_images(tableau)
    class_.cropping_images(tableau)
    img_path_1 = './daily_view.png'
    img_path_2 = './monthly_view.png'
    img_path_3 = './analytics/sex.png'
    img_path_4 = './analytics/age.png'
    img_path_5 = './analytics/regions.png'
    img_path_6 = './analytics/days.png'
    img_path_7 = './analytics/device_brand.png'
    img_path_8 = './analytics/returning_visitor.png'
    img_path_9 = './analytics/categories.png'

    pr.add_imagen(img_path_1,1)
    pr.add_imagen(img_path_2,2)
    pr.add_imagen(img_path_3,4)
    pr.add_imagen(img_path_4,5)
    pr.add_imagen(img_path_5,6)
    pr.add_imagen(img_path_6,7)
    pr.add_imagen(img_path_7,8)
    pr.add_imagen(img_path_8,9)
    pr.add_imagen(img_path_9,10)

    Robot(tableau, ad_manager_seller, start_date, end_date, pr)

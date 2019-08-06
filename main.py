from py_supermetrics import Integration
from py_tableau import Tableau_extractor
from py_pptx import PowerPointer
from py_cropping import DEV_cropping_images
from pdf2image import convert_from_path
from ventana_ui import *

import time
import os
import sys
import threading

class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.generar.clicked.connect(self.launch_Robot_Thread)

    def actualizar(self):

        self.status.setText("¡Acabas de hacer clic en el botón!")

        if self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text() and self.lineEdit_5.text():

            self.status.setText("Corriendo reporte. . .")

            tableau = self.lineEdit.text()
            ad_manager_seller = self.lineEdit_2.text()
            start_date = self.lineEdit_3.text()
            end_date = self.lineEdit_4.text()
            reporting_route = self.lineEdit_5.text()
            generar_reporte(tableau, ad_manager_seller, start_date, end_date, reporting_route, self)

        else:
            self.status.setText("Falta información !")

    def launch_Robot_Thread(self):
        t = threading.Thread(target=self.actualizar)
        t.start()

def current_path(dir_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, dir_path)
    return os.path.join(".", dir_path)

def Robot(Tableau_Store, seller, start_date, end_date, pr, self):

    admanager_query = 'https://supermetrics.com/api/v1/getData?metrics=TOTAL_INVENTORY_LEVEL_IMPRESSIONS%2CTOTAL_INVENTORY_LEVEL_CLICKS%2CTOTAL_INVENTORY_LEVEL_CTR_perc&dimensions=LINE_ITEM_NAME&filters=LINE_ITEM_NAME%3D%40MLC%3BLINE_ITEM_NAME%3D%40{0}&maxResults=1000&dateRangeType=custom&start-date={1}&end-date={2}&profiles=%5B%7B%22ID%22%3A%22105773011%22%2C%22name%22%3A%22Mercado%20Libre%22%7D%5D&otherParams=%5B%5D&dataSource=DFP&dsUser=gabriel.salinger%40mercadolibre.cl&apiKey=api_JRaerw456ubQqUuWDKwoJ37k4sMfs79o6VEledEHz1MB33OorUV0KpWiWG7oqiq3WAzs9BQHi2B9cuqh42ijdtO_rzr7TqCBVokW'.format(seller, start_date, end_date)

    query_device = 'https://supermetrics.com/api/v1/getData?metrics=TOTAL_INVENTORY_LEVEL_IMPRESSIONS%2CTOTAL_INVENTORY_LEVEL_CLICKS%2CTOTAL_INVENTORY_LEVEL_CTR_perc&dimensions=DEVICE_CATEGORY_NAME&filters=ORDER_NAME%3D%40{0}%3BORDER_NAME%3D%40MLC&maxResults=1000&dateRangeType=custom&start-date={1}&end-date={2}&profiles=%5B%7B%22ID%22%3A%22105773011%22%2C%22name%22%3A%22Mercado%20Libre%22%7D%5D&otherParams=%5B%5D&dataSource=DFP&dsUser=gabriel.salinger%40mercadolibre.cl&apiKey=api_JRaerw456ubQqUuWDKwoJ37k4sMfs79o6VEledEHz1MB33OorUV0KpWiWG7oqiq3WAzs9BQHi2B9cuqh42ijdtO_rzr7TqCBVokW'.format(seller, start_date, end_date)

    query_l2 = 'https://supermetrics.com/api/v1/getData?metrics=TOTAL_INVENTORY_LEVEL_IMPRESSIONS%2CTOTAL_INVENTORY_LEVEL_CLICKS%2CTOTAL_INVENTORY_LEVEL_CTR_perc&dimensions=AD_UNIT_NAME&filters=ORDER_NAME%3D%40{0}%3BORDER_NAME%3D%40MLC&maxResults=10&dateRangeType=custom&start-date={1}&end-date={2}&profiles=%5B%7B%22ID%22%3A%22105773011%22%2C%22name%22%3A%22Mercado%20Libre%22%7D%5D&otherParams=%5B%5D&dataSource=DFP&dsUser=gabriel.salinger%40mercadolibre.cl&apiKey=api_JRaerw456ubQqUuWDKwoJ37k4sMfs79o6VEledEHz1MB33OorUV0KpWiWG7oqiq3WAzs9BQHi2B9cuqh42ijdtO_rzr7TqCBVokW'.format(seller, start_date, end_date)

    class_ = Integration()
    data = class_.get_data(admanager_query)
    data2 = class_.get_data(query_device)
    data3 = class_.get_data(query_l2)

    if data["notes"]["status"] == 'success':
        ad_manager = data["data"]
        pr.add_table(ad_manager, 'Advertising Performance', 3)

    if data2["notes"]["status"] == 'success':
        ad_manager_2 = data2["data"]
        pr.add_table2(ad_manager_2, 'Advertising Performance', 4, False)

    if data3["notes"]["status"] == 'success':
        ad_manager_3 = data3["data"]
        pr.add_table2(ad_manager_3, 'Advertising Performance', 5, True)


    desktop = os.path.expanduser("~/Desktop")

    pr.save(desktop + os.sep + 'report_{0}'.format(seller))


def generar_reporte(tableau, ad_manager_seller, start_date, end_date, reporting_route, self):

    self.status.setText("Convertir gráficas. . .")

    os.environ["PATH"] += os.pathsep + \
    os.pathsep.join([current_path("poppler")])

    images = convert_from_path(reporting_route, 500)
    for image, i in zip(images, (range(len(images)))):
        image.save('analytics' + os.sep + 'analytics.png', 'PNG')

    self.status.setText("Recortando informe. . .")

    DEV_cropping_images(reporting_route)

    self.status.setText("Creando PPT. . .")

    pr = PowerPointer()
    pr.first_slide()


    self.status.setText("Sacando performance . . .")

    class_ = Tableau_extractor()
    class_.get_images(tableau)
    class_.cropping_images(tableau)

    self.status.setText("Agregando imágenes. . . ")

    img_path_1 = 'monthly_view.png'
    img_path_2 = 'daily_view.png'
    img_path_3 = 'analytics'+ os.sep + 'trafico.png'
    img_path_12 = 'analytics'+ os.sep + 'insights.png'
    img_path_4 = 'analytics'+ os.sep + 'sex.png'
    img_path_5 = 'analytics'+ os.sep + 'age.png'
    img_path_6 = 'analytics'+ os.sep + 'regions.png'
    img_path_7 = 'analytics'+ os.sep + 'days.png'
    img_path_8 = 'analytics'+ os.sep + 'type_device.png'
    img_path_9 = 'analytics'+ os.sep + 'device_brand.png'
    img_path_10 = 'analytics'+ os.sep + 'returning_visitor.png'
    img_path_11 = 'analytics'+ os.sep + 'categories.png'

    pr.add_imagen(img_path_1,1)
    pr.add_imagen(img_path_2,2)
    pr.add_imagen(img_path_3,6)
    pr.add_imagen(img_path_12,6)
    pr.add_imagen(img_path_4,7)
    pr.add_imagen(img_path_5,8)
    pr.add_imagen(img_path_6,9)
    pr.add_imagen(img_path_7,10)
    pr.add_imagen(img_path_8,11)
    pr.add_imagen(img_path_9,12)
    pr.add_imagen(img_path_10,13)
    pr.add_imagen(img_path_11,14)

    Robot(tableau, ad_manager_seller, start_date, end_date, pr, self)
    self.status.setText("Reporte terminado ")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

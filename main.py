"""
AUTOMATIZACIÓN DE REPORTES
Consultas a Nicolás Vega
ndvega@uc.cl / ext_nicovega@mercadolibre.com
"""
from py_supermetrics import Integration
from py_tableau import Tableau_extractor
from py_pptx import PowerPointer
from py_cropping import DEV_cropping_images
from py_apimeli import MELIntegration
from pdf2image import convert_from_path
from interface import *

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

        if self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_5.text():

            self.status.setText("Corriendo reporte. . .")
            tableau = self.lineEdit.text()
            ad_manager_seller = self.lineEdit_2.text()
            reporting_route = self.lineEdit_5.text()
            generar_reporte(tableau, ad_manager_seller, reporting_route, self)

        else:
            self.status.setText("Falta información !")

    def launch_Robot_Thread(self):
        t = threading.Thread(target=self.actualizar)
        t.start()

def current_path(dir_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, dir_path)
    return os.path.join(".", dir_path)

def Robot(Tableau_Store, seller, pr, self):

    desktop = os.path.expanduser("~/Desktop")
    pr.save(desktop + os.sep + 'report_{0}'.format(seller))


def generar_reporte(tableau, ad_manager_seller, reporting_route, self):

    self.status.setText("Convertir gráficas. . .")

    os.environ["PATH"] += os.pathsep + \
    os.pathsep.join([current_path("poppler")])

    images = convert_from_path(reporting_route, 500)

    p = 0

    for image, i in zip(images, (range(len(images)))):
        if p == 0:
            image.save('analytics' + os.sep + 'analytics.png', 'PNG')
            p += 1
        else:
            image.save('analytics' + os.sep + 'tables.png', 'PNG')

    self.status.setText("Recortando informe. . .")

    DEV_cropping_images(reporting_route)

    self.status.setText("Creando PPT. . .")

    pr = PowerPointer()
    pr.first_slide()

    self.status.setText("Sacando performance . . .")

    class_ = Tableau_extractor()
    class_.get_images(tableau)
    class_.cropping_images(tableau)

    self.status.setText("Sacando fotos . . .")

    class__ = MELIntegration()
    class__.filter('https://api.mercadolibre.com/sites/MLC/brands', ad_manager_seller)

    imagenes = os.listdir("images")

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

    ad_img_path_1 = 'analytics'+ os.sep + 'formatos.png'
    ad_img_path_2 = 'analytics'+ os.sep + 'ad_devices.png'
    ad_img_path_3 = 'analytics'+ os.sep + 'ad_categories.png'

    pr.add_imagen(img_path_1,1)
    pr.add_imagen(img_path_2,2)

    #ad manager
    pr.add_imagen(ad_img_path_1,3)
    pr.add_imagen(ad_img_path_2,4)
    pr.add_imagen(ad_img_path_3,5)

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

    for image_path in imagenes:
        pr.add_imagen('images'+ os.sep + image_path, 16)

    Robot(tableau, ad_manager_seller, pr, self)
    self.status.setText("Reporte terminado")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

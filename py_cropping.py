from PyPDF2 import PdfFileReader,PdfFileWriter
from pdf2image import convert_from_path
import cv2
import os
import time


def DEV_cropping_images(reporting_route):

    reporting = cv2.imread('analytics'+ os.sep + 'analytics.png')
    tables = cv2.imread('analytics'+ os.sep + 'tables.png')

    # [x arriba -> x abajo]
    #[ izq -> derecha]

    age = reporting[500:2550, 0:2800]
    cv2.imwrite('analytics'+ os.sep + 'age.png', age)

    device_brand = reporting[2600:4400, 0:2500]
    cv2.imwrite('analytics'+ os.sep + 'device_brand.png', device_brand)

    returning = reporting[2650:4700, 2550:5350]
    cv2.imwrite('analytics'+ os.sep + 'returning_visitor.png', returning)

    sex = reporting[600:2450, 2800:5000]
    cv2.imwrite('analytics'+ os.sep + 'sex.png', sex)

    region = reporting[0:2600, 5050:7800]
    cv2.imwrite('analytics'+ os.sep + 'regions.png', region)

    days = reporting[2650:4700, 5350:8000]
    cv2.imwrite('analytics'+ os.sep + 'days.png', days)

    categories = reporting[0:2650, 7850:11000]
    cv2.imwrite('analytics'+ os.sep + 'categories.png', categories)

    insights = reporting[3200:4500, 8500:11000]
    cv2.imwrite('analytics'+ os.sep + 'insights.png', insights)

    trafico = reporting[4650:6500, 0:3600]
    cv2.imwrite('analytics'+ os.sep + 'trafico.png', trafico)

    type_device = reporting[4700:6500, 3650:6000]
    cv2.imwrite('analytics'+ os.sep + 'type_device.png', type_device)

    formatos = tables[750:3200, 500:4450]
    cv2.imwrite('analytics'+ os.sep + 'formatos.png', formatos)

    ad_devices = tables[750: 1700, 4455:8000]
    cv2.imwrite('analytics'+ os.sep + 'ad_devices.png', ad_devices)

    ad_categories = tables[1850: 2800, 4455:8000]
    cv2.imwrite('analytics'+ os.sep + 'ad_categories.png', ad_categories)

    cv2.waitKey(0)

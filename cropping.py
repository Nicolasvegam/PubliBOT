from PyPDF2 import PdfFileReader,PdfFileWriter
from pdf2image import convert_from_path
import cv2 #Cropping
from wand.image import Image
from wand.color import Color

def cropping_images():

    print("[CROPPING IMAGES FROM PDF TO PNG]\n")

    with open("reporting.pdf", "rb") as in_f:
        input1 = PdfFileReader(in_f)
        output1 = PdfFileWriter()
        numPages = input1.getNumPages()

        for i in range(numPages):
            page = input1.getPage(i)
            page.mediaBox.lowerRight = (0, 0)
            page.mediaBox.lowerLeft = (0, 600)

            page.mediaBox.upperRight = (400, 0)
            page.mediaBox.upperLeft = (0, 300)
            output1.addPage(page)

            with open("analytics/age.pdf", "wb") as out_f:
                output1.write(out_f)

    with open("reporting.pdf", "rb") as in_f:
        input2 = PdfFileReader(in_f)
        output2 = PdfFileWriter()

        numPages = input1.getNumPages()

        for i in range(numPages):
            page = input2.getPage(i)
            page.mediaBox.lowerRight = (0, 0)
            page.mediaBox.lowerLeft = (0, 300)

            page.mediaBox.upperRight = (370, 0)
            page.mediaBox.upperLeft = (0, 50)
            output2.addPage(page)

            with open("analytics/device_brand.pdf", "wb") as out_f:
                output2.write(out_f)

    with open("reporting.pdf", "rb") as in_f:
        input3 = PdfFileReader(in_f)
        output3 = PdfFileWriter()

        numPages = input1.getNumPages()

        for i in range(numPages):
            page = input3.getPage(i)
            page.mediaBox.lowerRight = (0, 0)
            page.mediaBox.lowerLeft = (0, 300)
            page.mediaBox.upperRight = (770, 0)
            page.mediaBox.upperLeft = (360, 20)
            output3.addPage(page)

            with open("analytics/returning_visitor.pdf", "wb") as out_f:
                output3.write(out_f)
#
    with open("reporting.pdf", "rb") as in_f:
        input4 = PdfFileReader(in_f)
        output4 = PdfFileWriter()

        numPages = input1.getNumPages()

        for i in range(numPages):
            page = input4.getPage(i)
            page.mediaBox.lowerRight = (410, 600)
            page.mediaBox.upperLeft = (710, 300)
            output4.addPage(page)

            with open("analytics/sex.pdf", "wb") as out_f:
                output4.write(out_f)

    with open("reporting.pdf", "rb") as in_f:
        input5 = PdfFileReader(in_f)
        output5 = PdfFileWriter()

        numPages = input1.getNumPages()

        for i in range(numPages):
            page = input5.getPage(i)
            page.mediaBox.lowerLeft = (1130, 300)
            output5.addPage(page)

            with open("analytics/categories.pdf", "wb") as out_f:
                output5.write(out_f)

#
    with open("reporting.pdf", "rb") as in_f:
        input6 = PdfFileReader(in_f)
        output6 = PdfFileWriter()

        numPages = input1.getNumPages()

        for i in range(numPages):
            page = input6.getPage(i)
            page.mediaBox.lowerRight = (720, 670)
            page.mediaBox.upperLeft = (1130, 300)
            output6.addPage(page)

            with open("analytics/regions.pdf", "wb") as out_f:
                output6.write(out_f)

    with open("reporting.pdf", "rb") as in_f:
        input7 = PdfFileReader(in_f)
        output7 = PdfFileWriter()

        numPages = input1.getNumPages()

        for i in range(numPages):
            page = input7.getPage(i)
            page.mediaBox.lowerRight = (770, 280)
            page.mediaBox.upperLeft = (1150, 0)
            output7.addPage(page)

            with open("analytics/days.pdf", "wb") as out_f:
                output7.write(out_f)

def convert_images():

    #print("[CONVERTING IMAGES FROM PDF TO PNG]\n")

    with Image(filename="analytics/age.pdf", resolution=300) as img:
        #print("age: Size width:{0} Size height: {1}\n", img.width, img.height)
        img.save(filename="analytics/age.png")

    with Image(filename="analytics/sex.pdf", resolution=300) as img:
        #print("sex: Size width:{0} Size height: {1}\n", img.width, img.height)
        img.format = 'jpeg'
        img.save(filename="analytics/sex.png")

    with Image(filename="analytics/categories.pdf", resolution=300) as img:
        #print("categories: Size width:{0} Size height: {1}\n", img.width, img.height)
        img.format = 'jpeg'
        img.save(filename="analytics/categories.png")

    with Image(filename="analytics/days.pdf", resolution=300) as img:
        #print("days: Size width:{0} Size height: {1}\n", img.width, img.height)
        img.format = 'jpeg'
        img.save(filename="analytics/days.png")

    with Image(filename="analytics/device_brand.pdf", resolution=300) as img:
        #print("device_brand: Size width:{0} Size height: {1}\n", img.width, img.height)
        img.format = 'jpeg'
        img.save(filename="analytics/device_brand.png")

    with Image(filename="analytics/returning_visitor.pdf", resolution=300) as img:
        #print("returning_visitor: Size width:{0} Size height: {1}\n", img.width, img.height)
        img.format = 'jpeg'
        img.save(filename="analytics/returning_visitor.png")

    with Image(filename="analytics/regions.pdf", resolution=300) as img:
        #print("regions: Size width:{0} Size height: {1}\n", img.width, img.height)
        img.format = 'jpeg'
        img.save(filename="analytics/regions.png")


cropping_images()
convert_images()

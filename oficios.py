import os
from os.path import isfile, join
import PyPDF2
from PyPDF2 import PdfFileReader

# Obtener la ruta actual
ruta = os.path.abspath(os.getcwd())
entrada = ruta + "/entrada/"
salida = ruta + "/salida/"

# Listas para guardar los números de las hojas
inferior = []
superior = []


def error():
    print("Error, solo se puede separar un archivo a la vez")

def extraer():
    # El nombre del archivo
    base_path = entrada
    file_ls = [f for f in os.listdir(base_path) if isfile(join(base_path, f))]
    oficio = str(file_ls[0])
    oficio_1 = oficio[0:-4]
    # print(oficio_1)
    nuevos = len(inferior)

    # Crear los objetos para manipulación de PDF
    pdfFileObj = open(entrada + oficio, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Contar el número de oficios nuevos a crear
    for nu in range(0,  nuevos):
        pdfWriter = PyPDF2.PdfFileWriter()
        outputpdf = os.path.join(salida + oficio_1 + '_' + str(nu+1) + '_de_' + str(nuevos+1) + '.pdf')
        for page in range(inferior[nu]-1, superior[nu]):
            pdfWriter.addPage(pdfReader.getPage(page))

            # Guardar el nuevo archivo de PDF
            with open(outputpdf, "wb") as f:
                pdfWriter.write(f)

    # Obtener el número de páginas
    n_pag = pdfReader.numPages
    remanente = n_pag % 25


    if remanente > 0:
        pdfWriter_1 = PyPDF2.PdfFileWriter()
        outputpdf_1 = os.path.join(salida + oficio_1 + '_' + str(nuevos+1) + '_de_' + str(nuevos + 1) + '.pdf')
        # print(outputpdf_1)
        for page_1 in range(superior[nuevos-1], n_pag):
            pdfWriter_1.addPage(pdfReader.getPage(page_1))

            # Guardar el nuevo archivo de PDF
            with open(outputpdf_1, "wb") as f_1:
                pdfWriter_1.write(f_1)


def oficios():

    # Verificar que se trabaje con un solo archivo
    base_path = entrada
    file_ls = [f for f in os.listdir(base_path) if isfile(join(base_path, f))]
    # print(file_ls)

    if len(file_ls)>1:
        error()
    else:
        oficio = str(file_ls[0])

        # Obtener el número de páginas
        with open(os.path.join(entrada + oficio), "rb") as pdf_file:
            pdf_reader = PdfFileReader(os.path.join(entrada + oficio))
            n_pag = pdf_reader.numPages
        # print(n_pag)
        division = n_pag//25
        # print(division)
        # remanente = n_pag % 25
        # print(remanente)


        # Contador cada 10 hojas
        for n in range(1, division + 1):

            n_25 = n * 25
            n_1 = n_25 - 24
            # print(n_1)
            inferior.append(n_1)
            # print(n_25)
            superior.append(n_25)
        # El número de archivos nuevos a crear

        extraer()
        # print(inferior)
        # print(superior)

oficios()

inferior.clear()
superior.clear()
division = 0

print("Rutina terminada")

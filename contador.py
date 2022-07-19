import os
from PyPDF2 import PdfFileReader

# Obtener la ruta actual
ruta = os.path.abspath(os.getcwd())

carpeta = ruta + "\entrada"
oficio = "ASEA_UGI_DGGOI_3135_2021.pdf"
ruta_c = os.path.join(carpeta + oficio)

with open(ruta_c, "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)

    print(f"The total number of pages in the pdf document is {pdf_reader.numPages}")
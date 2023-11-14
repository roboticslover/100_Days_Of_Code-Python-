from PyPDF2 import pdfWriter
import os

merger = PdfWriter()
files = os.listdir('clutter')

for file in files:
    merger.append(fileobj=f'clutter/{file}')

merger.write('clutter/merger.pdf')
merger.close()

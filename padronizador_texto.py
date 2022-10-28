# importa as bibliotecas necessárias
import PyPDF2
import re
import os
# -*- coding: utf-8 -*-
import sys
import codecs

page_content =""
pasta = 'docs-pdf'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        print(os.path.join(diretorio, arquivo))
        # Abre o arquivo pdf 
        # lembre-se que para o windows você deve usar essa barra -> / 
        # lembre-se também que você precisa colocar o caminho absoluto
        pdf_file = open(os.path.join(diretorio, arquivo), 'rb')

        #Faz a leitura usando a biblioteca
        read_pdf = PyPDF2.PdfFileReader(pdf_file)

        # pega o numero de páginas
        number_of_pages = read_pdf.getNumPages()

        
        for n in range(read_pdf.getNumPages()):
          page = read_pdf.getPage(n)
          page_content += page.extractText()
print(page_content)

with open('extracao_python_doc.txt', 'w+') as f: 
            for items in page_content: 
                f.write('%s\n' %items) 
            f.close()
# -*- coding: utf-8 -*-
# importa as bibliotecas necessárias
import PyPDF2
import re
import os
# -*- coding: utf-8 -*-
import sys
import codecs
import pandas as pd

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

#--------------------------------------------------------------------------------
# with open("palavras.txt",'r') as f: 
  # artigos = f.read() # Lê o arquivo completo e atribui a variável
artigos = page_content 

print(artigos[:500]) #  mostra as primeiras 500 letras
"""# **2 - Imprimindo tamanho dos arquivos em caractéres**"""

print(len(artigos)) #conta os caractéres e não o número de palavras
"""# **3 - Imprimindo tamanho dos arquivos em tokens**"""

len(artigos.split()) #conta palavras repetidas, além de vírgulas e pontuação
print(len(artigos.split()))

artigos2 = artigos 
# artigos =  artigos + '\n' + palavras + '\n' + palavras2 + '\n' + palavras3

"""# **4 - Minha Função para Separar Palavras**"""
# Tentativa de criar uma forma de separar palavras
def sep(string):
  lista = ['&','’','’','…','‘','’''&','“','”',',',
           '.' , ';' , '?',"!","#","$",":","+","(",")","-","=",
           "´","`","'",'"',']','[','{','}','@','%',"*",'>','<',
           '^','~','1','2','3','4','5','6','7','8','9','0','_',
           '/','\\','€','—','|','😮','😀','🙂','¨','²','³','–',
           '\u200b\u200bpodem','→','➢','Altura²','√','―','|Posição',
            '–dev','😊','😂','♥','°','||','⁸','⁵²','¢','—algo','–add',
           '←','←número','😉','¹¹','¯','©','\u200b','•','\u200b\u200b','⁵']
  for item in lista:
    string = string.replace(item,' ')

  string = string.split()
  return string

"""## **4.1 - testes**"""

x = sep(artigos2)
len(x)

"""## **4.2 Retirando duplicidades**"""

# Retirando duplicidade de palavras
import pandas as pd
lista_palavras_lower = []
for palavra in x:
  lista_palavras_lower.append(palavra.lower())
palavras_unicas = list(set(lista_palavras_lower))
print(palavras_unicas[:50])
print('Quantidade de Palavras: ', len(palavras_unicas))

"""# **5 - Minha outra Função**"""

# Função que usa o isalpha para pegar aquilo que não for alfabético e descartar
def separar_inteligente(texto_exemplo):
  for item in texto_exemplo:
    if not item.isalpha():
      texto_exemplo = texto_exemplo.replace(item,' ')
  texto_exemplo = texto_exemplo.split()
  return texto_exemplo

"""## **5.1 - testes**"""

resultado_sep = separar_inteligente(artigos2)
print(resultado_sep[:5])
print(len(resultado_sep))

"""## **5.2 Retirando duplicidades**"""

# Retirando duplicidade de palavras
lista_palavras_2_lower = []
for palavra in resultado_sep:
    lista_palavras_2_lower.append(palavra.lower())
palavras_unicas_2 = list(set(lista_palavras_2_lower))
print(palavras_unicas_2[:5])
print('Quantidade de Palavras: ', len(palavras_unicas_2))

"""# **6 - Usando NLTK para Separar palavras**

## **6.1 - Importando biblioteca ntlk**
"""
import nltk
nltk.download('punkt')

"""## **6.4 - Função Separa Palavras - isalpha()**"""

def separa_palavras(lista_tokens):
  lista_palavras = []
  for token in lista_tokens:
    if token.isalpha():
      lista_palavras.append(token)
  return lista_palavras

"""## **6.6 - Função Normalização - tudo minúsculo**"""

# verificando se tenho o mesmo tipo de palavras porém escritas de formas diferentes
def normalizacao(lista_palavras):
  lista_normalizada = []
  for palavra in lista_palavras:
    lista_normalizada.append(palavra.lower())
  return lista_normalizada


"""## **6.7 - Rodando tudo até aqui**"""

# lista_normalizada = normalizacao(lista_palavras)
# print(lista_normalizada[:5])
# print(len(lista_normalizada))

"""## **6.8 - Removendo repetições - SET()**"""
lista_tokens = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(lista_tokens)
# print(f'O número de palavras é de : {len(lista_palavras)}')
lista_palavras_teste = lista_palavras.copy()
lista_normalizada = normalizacao(lista_palavras)

# O set garante apenas o conjunto da lista, sem repetições
lista_sem_repeticoes = set(lista_normalizada)
len(lista_sem_repeticoes)
# with open('muitas_palavras.txt', 'w+') as f: 
#   for items in lista_sem_repeticoes: 
#       f.write('%s\n' %items) 
#   f.close()


# Obtendo palavras portugues
df_portugues = pd.read_csv('https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt',encoding='utf-8')
lista_portugues = df_portugues["a"].values.tolist()
df_ingles = pd.read_csv('unigram_freq.csv')
lista_ingles = df_ingles["word"].values.tolist()
listao = lista_sem_repeticoes + lista_ingles + lista_portugues
# lista_minha_copia = pd.read_csv('python-words.csv')
with open('muitas_palavras.txt', 'w') as arquivo:
    arquivo.write(str(listao))
    arquivo.close()
print("terminou")


import time
from numpy import integer 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options
import pandas as pd

def burlar(driver):
    caixa = driver.find_element(by=By.XPATH, value='//*[@id="rd-checkbox_field-l1pbxk0q"]') 
    caixa.click()
    time.sleep(1)
    scrap = driver.find_element(by=By.XPATH, value='//*[@id="math_expression"]') 
    texto = scrap.text
    texto = texto.replace("= ?","")
    lista_numeros = texto.split("+")
    nova_lista = []
    for i in lista_numeros:
        nova_lista.append(int(i.strip()))
    soma = 0
    for num in nova_lista:
        soma +=num
    calculo = driver.find_element(by=By.XPATH, value='//*[@id="captcha"]') 
    calculo.send_keys(soma)
    seguir = driver.find_element(by=By.XPATH, value='//*[@id="rd-button-joq3m2m7"]') 
    seguir.click()
    seguir.click()
    new_list.remove(p)
    print(p)
    time.sleep(5)
    voltar = driver.find_element(by=By.XPATH, value='//*[@id="rd-button-l8xo0ikm"]') 
    voltar.click()

# Obtendo palavras portugues
df = pd.read_csv('https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt',encoding='utf-8')
lista = df["a"].values.tolist()
# df = pd.read_csv('unigram_freq.csv')
# lista = df["word"].values.tolist()
new_list = []
for palavra in lista:
    if len(str(palavra)) == 6:
        #print(palavra)
        if str(palavra)[2] == "n" \
            and str(palavra)[-1] == "r" \
            and str(palavra)[0]=="d" \
            and str(palavra)[3]=="d":
            new_list.append(str(palavra))
print(len(new_list))

chrome_options = Options()
chrome_options.add_argument("--kiosk")
driver =  driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options) 
driver.get("https://even.tdigi.com.br/tw-pythonbr") 
driver.maximize_window()

name = driver.find_element(by=By.XPATH, value='//*[@id="rd-text_field-l1pbxk0l"]') 
name.send_keys("Igor Adriano de Carvalho Rodrigues") 
time.sleep(1)
cargo = driver.find_element(by=By.XPATH, value='//*[@id="rd-email_field-l1pbxk0m"]') 
cargo.send_keys(r"igorrodriguesdmx@hotmail.com") 
time.sleep(1)
cargo = driver.find_element(by=By.XPATH, value='//*[@id="rd-text_field-l1pbxk0n"]') 
cargo.send_keys("Analista de Dados") 
time.sleep(1)
palavra = driver.find_element(by=By.XPATH, value='//*[@id="rd-text_field-l1pbxk0o"]') 
palavra.send_keys(new_list[0]) 
time.sleep(1)
caixa = driver.find_element(by=By.XPATH, value='//*[@id="rd-checkbox_field-l1pbxk0q"]') 
caixa.click()
time.sleep(1)
scrap = driver.find_element(by=By.XPATH, value='//*[@id="math_expression"]') 
texto = scrap.text
texto = texto.replace("= ?","")
lista_numeros = texto.split("+")
nova_lista = []
for i in lista_numeros:
    nova_lista.append(int(i.strip()))
soma = 0
for num in nova_lista:
    soma +=num
calculo = driver.find_element(by=By.XPATH, value='//*[@id="captcha"]') 
calculo.send_keys(soma)

seguir = driver.find_element(by=By.XPATH, value='//*[@id="rd-button-joq3m2m7"]') 
seguir.click()
seguir.click()
new_list.remove(new_list[0])
print(new_list[0])
time.sleep(5)
voltar = driver.find_element(by=By.XPATH, value='//*[@id="rd-button-l8xo0ikm"]') 
voltar.click()

        

for p in new_list[1:]:
    try:
        burlar(driver)
    except:
        with open('palavras.txt', 'w+') as f: 
            for items in new_list: 
                f.write('%s\n' %items) 
            f.close()
      

  
  


    
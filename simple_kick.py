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

# Obtendo palavras portugues
# df = pd.read_csv('https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt',encoding='utf-8')
# lista = df["a"].values.tolist()
df = pd.read_csv('end_game.txt')
lista = df["x"].values.tolist()
new_list = []
for palavra in lista:
    if len(str(palavra)) == 6:
        #print(palavra)
        if str(palavra)[2] == "n":
            new_list.append(str(palavra.lower()))
new_list = sorted(new_list)
with open('lista_inicial.txt', 'w+') as f: 
    for items in new_list: 
        f.write('%s\n' %items) 
    f.close()

actual_list = new_list.copy()
for p in new_list:
    try:
        chrome_options = Options()
        chrome_options.add_argument("--kiosk")
        driver =  driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options) 
        driver.get("https://even.tdigi.com.br/tw-pythonbr") 
        driver.maximize_window()

        name = driver.find_element(by=By.XPATH, value='//*[@id="rd-text_field-l1pbxk0l"]') 
        name.send_keys("Igor Adriano de Carvalho Rodrigues") 
        time.sleep(1)
        cargo = driver.find_element(by=By.XPATH, value='//*[@id="rd-email_field-l1pbxk0m"]') 
        cargo.send_keys(r"igorrodriguesmdx@hotmail.com") 
        time.sleep(1)
        cargo = driver.find_element(by=By.XPATH, value='//*[@id="rd-text_field-l1pbxk0n"]') 
        cargo.send_keys("Analista de Dados") 
        time.sleep(1)
        palavra = driver.find_element(by=By.XPATH, value='//*[@id="rd-text_field-l1pbxk0o"]') 
        palavra.send_keys(p) 
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
        print(p)
        actual_list.remove(p)
        time.sleep(5)
        driver.close() 
    except:
        with open('lista_depois_que_quebrou.txt', 'w+') as f: 
            for items in actual_list: 
                f.write('%s\n' %items) 
            f.close()
      

  
  


    
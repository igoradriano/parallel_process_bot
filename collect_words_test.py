import pandas as pd
df = pd.read_csv('https://www.ime.usp.br/~pf/dicios/br-utf8.txt',encoding='utf-8')
lista = df["AC"].values.tolist()
print(list)
new_list = []
for palavra in lista:
    if len(palavra) == 6:
        #print(palavra)
        for letra in range(len(palavra)):
            if palavra[letra] == "n": 
                new_list.append(palavra)


# nova_lista = []
# for p in lista:
#     print(p)
#     # if p[2] =="n":
#     #     nova_lista.append(p)
# print(nova_lista)
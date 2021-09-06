import requests
import json
import pandas as pd
from math import ceil

#Autenticação
appkey = "38333295000"
keysecret = "4cea520a0e2a2ecdc267b75d3424a0ed"

###Parametros
NomeArquivo = "Verticais"
NomeApi = "ListarVerticais"
endPoint = "https://app.omie.com.br/api/v1/crm/verticais/"
RegistrosPagina = 20
NomeLista = "cadastros"


#Pegar o número de páginas que precisam ser processadas
param = {
  "pagina": 1,
  "registros_por_pagina": 1
}
jsonFile = {"call":NomeApi,"app_key":appkey,"app_secret":keysecret,"param":[param]}
arqv = requests.post(endPoint , json = jsonFile)
NumeroPaginas = ceil(arqv.json()["total_de_paginas"]/RegistrosPagina) + 1


#função de extração
def fExtracao(x):
    Temp_param = {
        "pagina": x,
        "registros_por_pagina": RegistrosPagina
    }
    Temp_jsonFile = {"call": NomeApi, "app_key": appkey, "app_secret": keysecret,
                     "param": [Temp_param]}
    Temp_arqv = requests.post(endPoint, json=Temp_jsonFile)
    arq = pd.json_normalize(Temp_arqv.json()[NomeLista])
    Temp_dataset = pd.DataFrame(arq)
    return Temp_dataset


##### Criacao de dataset
dataset = fExtracao(1)

for i in range(2,NumeroPaginas):
    data = fExtracao(i)
    dataset = dataset.append(data)


 #Salvar CSV
dataset.to_csv(NomeArquivo+".csv" , index = False , encoding ="utf-8-sig")
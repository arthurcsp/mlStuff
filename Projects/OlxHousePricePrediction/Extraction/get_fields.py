from bs4 import BeautifulSoup
import pandas as pd 
import requests
import time



def get_fields(codigo , descricao , link, page):
    ### Request
    try:
        houseRequest = requests.get(link , headers={'User-Agent': 'Mozilla/5.0'})
        assert houseRequest.status_code == 200 , 'Status code error'
    except:
        time.sleep(5)
        houseRequest = requests.get(link , headers={'User-Agent': 'Mozilla/5.0'})
        assert houseRequest.status_code == 200 , 'Status code error'

    ### Soup
    soup = BeautifulSoup(houseRequest.content, 'html.parser')
    fields ={}
    fields['Codigo'] = codigo
    fields['Descricao'] = descricao
    fields['Link'] = link
    fields['Page'] = page


    ### Value
    value = soup.find('div',{'data-testid' :'ad-price-wrapper'}).find('h2').get_text()
    fields['Valor'] = value

    #Details
    for i in soup.find('div',{'data-testid' :'ad-properties'}):
        detailType = i.find('dt').get_text()
        try:
            value =i.find('a').get_text()
        except:
            value =i.find('dd').get_text()
        fields[detailType]=value

    #Localization
    for i in soup.find_all('div',{'data-testid' :'ad-properties'})[1]:  
        detailType = i.find('dt').get_text()
        try:
            value =i.find('a').get_text()
        except:
            value =i.find('dd').get_text()
        fields[detailType]=value

    return fields
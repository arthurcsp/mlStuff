from bs4 import BeautifulSoup
import requests
from IPython.display import clear_output



def get_urls(link,pages):

    links= {}
    errors = []

    for page in range(1,pages + 1):  
        clear_output(wait = True)
    ### Request
        olxRequest = requests.get('{}?o={}'.format(link,page) , headers={'User-Agent': 'Mozilla/5.0'})
        try:
            assert olxRequest.status_code == 200 , 'Status code error {}'.format(olxRequest.status_code)  
        except:
            print('Status code error {} in page {}'.format(olxRequest.status_code,page) )
            errors.append(page)
            continue
    
    ### Soup
        soup = BeautifulSoup(olxRequest.content, 'html.parser')
        itens = soup.find('ul',{'id' : 'ad-list'})
        lista = itens.find_all('li')

    ### Urls
        urls = []
        for index,i in enumerate(lista):
            try:
                temp_href =i.find('a').get('href')
                temp_item =i.find('a').get('data-lurker_list_id')
                temp_title =i.find('a').get('title')        
        #print(temp_item)
                urls.append([temp_item, temp_title, temp_href])
            except:
                None
        
        links[page]=urls
        print(f'Página Atual: {page}')
        print(f'Páginas com erro: {errors}')
    return links 
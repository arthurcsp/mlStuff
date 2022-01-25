import requests as rq
import pandas as pd

def pos(adress):
    apikey= 'AIzaSyCzwko2fGEc3H9hj-qr9tF2i-H0EQllX3s'
   ## adress=  'AV. M, S/N , RESIDENCIAL JABAETÉ, vila velha'###'RUA ÚTE AMÉLIA GASTIN PÁDUA 124, SÃO TARCÍSIO'
    try:
        response = rq.get("https://maps.googleapis.com/maps/api/geocode/json?address="+adress+"&key="+apikey+"")
        respostas= response.json()
        place = respostas["results"][0]["geometry"]["location"]
        return([place['lat'],place['lng']])
    except:
        return([0,0])


def pos_testing(adress):
    apikey= 'AIzaSyCzwko2fGEc3H9hj-qr9tF2i-H0EQllX3s'
   ## adress=  'AV. M, S/N , RESIDENCIAL JABAETÉ, vila velha'###'RUA ÚTE AMÉLIA GASTIN PÁDUA 124, SÃO TARCÍSIO'
    response = rq.get("https://maps.googleapis.com/maps/api/geocode/json?address="+adress+"&key="+apikey+"")
    respostas= response.json()
    place = respostas
    return(place)





#print(pos_testing("Rua nossa senhora de fatima, 226 , Gloria , vila velha"))



# https://127.0.0.1:3030/api/BARRIO/INMUEBLE/TIPO
from bs4 import BeautifulSoup
import requests
import unicodedata
from flask import Flask, json, request


def pagina(num, barrio, inmueble, tipo):
    url = "https://www.properati.com.ar/s/" + barrio+"/" + inmueble + "/"+ tipo + "?page="+ str(num)
    response = requests.get(url)
    response.encoding = "utf-8"
    html = response.text
    dom = BeautifulSoup(html, features = "html.parser")
    fin = dom.find( attrs = {'class': 'StyledPagerButton-sq1exe-0 cFkGqv pager-next'} )
    
    return fin,dom


app = Flask(__name__)


@app.route("/<barrio>/<inmueble>/<tipo>")
def scrapeo(barrio,inmueble,tipo):
    fin , dom =pagina(1,barrio, inmueble, tipo)
    print(dom)
    return "hola"



app.run( port = 3030, host = '0.0.0.0' )










# num = 1    
# barrio= 'palermo'
# inmueble= 'departamento'
# tipo = 'alquiler'




# fin, dom = pagina(1, barrio, inmueble, tipo)
# #print(fin.text)
# id = 1
# propiedad =[]

# while fin != None:
    
#     anuncios = dom.find_all( attrs = { 'class' : 'StyledCard-n9541a-1 jWSYcc' } )
    
    
#     for anuncio in anuncios:
                
#         titulo = anuncio.find( attrs = { 'class' : 'StyledTitle-n9541a-4 bwJAej' } )
#         precio = anuncio.find( attrs = { 'class' : 'StyledPrice-sc-1wixp9h-0 bZCCaW' } )
#         expensas = anuncio.find( attrs = { 'class' : 'StyledMaintenanceFees-n9541a-6 cRsmn' } )
#         detalles = anuncio.find( attrs = { 'class' : 'StyledInfoIcons-n9541a-9 fgcFIO' } )
#         inmobiliaria = anuncio.find( attrs = { 'class' : 'seller-name' } )
        
#         if titulo: titulo = titulo.get_text()
#         if precio: precio= precio.get_text()
#         if expensas: expensas = unicodedata.normalize("NFKD", expensas.get_text()) 
#         if inmobiliaria: imobiliaria = inmobiliaria.get_text()
#         if detalles:
#             spans = detalles.find_all('span')
#             for span in spans:
#                 txt = span.get_text()
#                 if (txt.find('m²')>=0): m2 = txt
#                 if (txt.find('ambiente')>=0): ambientes = txt
#                 if (txt.find('baño')>=0): banios = txt
#         valor = {'id': id, 'precio': precio, 'expensas': expensas, 'm2': m2}
#         propiedad.append(valor)
#         id= id+1
#     #print(num, fin)
#     num= num + 1            
#     fin, dom= pagina(num, barrio, inmueble, tipo)
    
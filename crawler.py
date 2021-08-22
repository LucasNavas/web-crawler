import scrapy
import csv
import requests
import pandas as pd
from pandas.core.base import DataError
from pathlib import Path 
from dotenv import load_dotenv


data = pd.read_csv("listasites2.csv",sep=",")
data.columns = ["sites"]
rawsites = list(data.sites)

for x in range(len(rawsites)):
    url = rawsites[x]
    existe = False
    nomesite = ''
    nomeplataforma = ''
    cnpj = ''
    nomesocio = ''
    instagram = ''
    try:
        request = requests.get(url)
        print(request.status_code)
        if request.status_code == 200:
            existe = True
        elif request.status_code == 403:
            print("Acesso ao site bloqueado")
            existe = False
        else:
            existe = False
    except:
            existe = False
    print(existe)    


    class CrawlerKyraly(scrapy.Spider):
        name = 'CrawlerKyraly'
        if existe == True:
            start_urls = [url]
            def parse(self, response):
                header = ['URL', 'Nome', 'Plataforma', 'Telefone', 'CNPJ', 'Nome Socio', 'Instagram']
                site = str(response.css('html').get())
                title = str(response.css('title::text').get())
                nomesite = title
                if "nuvemshop" in site.lower():
                    print("Nuvemshop")
                    nomeplataforma = 'Nuvemshop'

                elif "vtex" in site.lower():
                    print("Vtex")
                    nomeplataforma = 'Vtex'

                elif "magento" in site.lower():
                    print("Magento")
                    nomeplataforma = 'Magento'
                
                elif "shopify" in site.lower():
                    print("Shopify")
                    nomeplataforma = 'Shopify'

                elif "linx" in site.lower():
                    print("Linx")
                    nomeplataforma = 'Linx'

                elif "lojaintegrada" in site.lower():
                    print("Loja Integrada")
                    nomeplataforma = 'Loja Integrada'

                elif "prestashop" in site.lower():
                    print("Prestashop")
                    nomeplataforma = 'Prestashop'

                elif "tray" in site.lower():
                    print("Tray")
                    nomeplataforma = 'Tray'

                elif "jetecommerce" in site.lower():
                    print("Jet E-commerce")
                    nomeplataforma = 'Jet E-commerce'

                else:
                    print("outra")
                    nomeplataforma = 'outra'


                header = ['URL', 'Nome', 'Plataforma', 'CNPJ', 'Telefone', 'Nome Socio', 'Instagram']
                data = [url, nomesite, nomeplataforma, 'sem valor','sem valor','sem valor','sem valor']
                with open('crawler.csv', 'w', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerow(data)
                    
#do lado de fora da def parse (linha 14), teremos que colocar o Looping para acessar todos os sites um de cada vez, alterando a variável Site da linha 3
#Teremos que fazer dentro da def parse todas as condições para pegar a plataforma, e caso não a encontremos, definir como outro
#Temos que retornar todas essas informações conseguidas para dentro de uma arquivo .csv






"""
- Terminar verificação de plataforma
- Envio dessas verificações pra um arquivo csv
- Pegar tag <title> e enviar como nome da empresa


"""
















"""

header = ['URL', 'Nome', 'Plataforma', 'CNPJ', 'Nome Socio', 'Instagram']
data = [1+x, 2+x, 3+x, 4+x]
with open('crawler.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

 """  
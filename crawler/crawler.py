#Caso você já tenha uma lista filtrada, nomeie ela como listafiltrada.csv e coloque na pasta filteredcsv, e execute o arquivo por aqui com o comando scrapy runspider crawler/crawler.py
import scrapy
import csv
import os
import requests
import pandas as pd
from pandas.core.base import DataError
from pathlib import Path 
from dotenv import load_dotenv

sitesfiltrados = []
titulosfiltrados = []
plataforma = []
x = 0
existe = False
nomesite = ''
nomeplataforma = ''


data = pd.read_csv(r"filteredcsv\listafiltrada.csv",sep=",")
data.columns = ["sites"]
sitesfiltrados = list(data.sites)

class CrawlerKyraly(scrapy.Spider):
        name = 'CrawlerKyraly'
        start_urls = [sitesfiltrados[0]]
        def parse(self, response):
            global x
            site = str(response.css('html').get())
            if "nuvemshop" in site.lower():
                nomeplataforma = 'Nuvemshop'

            elif "vtex" in site.lower():
                nomeplataforma = 'Vtex'

            elif "magento" in site.lower():
                nomeplataforma = 'Magento'
            
            elif "shopify" in site.lower():
                nomeplataforma = 'Shopify'

            elif "linx" in site.lower():
                nomeplataforma = 'Linx'

            elif "lojaintegrada" in site.lower():
                nomeplataforma = 'Loja Integrada'

            elif "prestashop" in site.lower():
                nomeplataforma = 'Prestashop'

            elif "tray" in site.lower():
                nomeplataforma = 'Tray'

            elif "jetecommerce" in site.lower():
                nomeplataforma = 'Jet E-commerce'
            
            elif "wapstore" in site.lower():
                nomeplataforma = 'Wap Store'

            else:
                nomeplataforma = 'Plataforma desconhecida'

            title = str(response.css('title::text').get())
            contador = x+1
            print('Site nº%s da lista de sites.' % contador)
            print("URL do site sendo que está verificado: "+sitesfiltrados[x])
            if title != 'None':
                titulosfiltrados.append(title)
            else:
                titulosfiltrados.append("Titulo Desconhecido")
            plataforma.append(nomeplataforma)
            x+=1
            if x < len(sitesfiltrados):
                next_site = sitesfiltrados[x]
            else:
                next_site = None
            if next_site is not None:
                next_site = response.urljoin(next_site)
                yield response.follow(next_site, callback=self.parse)
            else:
                with open(r'arquivocsv\crawler.csv', 'w', encoding='UTF8') as f:
                    header = ['URL', 'Nome', 'Plataforma']
                    writer = csv.writer(f, lineterminator = '\n')
                    writer.writerow(header)
                    for y in range(len(sitesfiltrados)):
                        writer.writerow([sitesfiltrados[y], titulosfiltrados[y],plataforma[y]])
                        y=y+1




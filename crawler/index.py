#Este arquivo é o que deve ser executado, ele é a raiz de todo código

import csv
import os
import requests
import time
import pandas as pd
from pathlib import Path 

os.system("echo Inicializando...")
data = pd.read_csv(r"arquivocsv\listasites.csv",sep=",")
data.columns = ["sites"]
rawsites = list(data.sites)
sitesfiltrados = []
titulosfiltrados = []
plataforma = []
x = 0

with open(r'filteredcsv\listafiltrada.csv', 'w', encoding='UTF8') as f:
    header = ['sites']
    writer = csv.writer(f, lineterminator = '\n')
    writer.writerow(header)

    for x in range(len(rawsites)):
        url = rawsites[x]
        existe = False
        nomesite = ''
        nomeplataforma = ''
        cnpj = ''
        nomesocio = ''
        instagram = ''
        timeout = 5 #segundos
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            try:
                request = requests.get(url)
                contador = x + 1
                print("Site",contador,"de",len(rawsites))
                print("Verificando URL "+url)
                if request.status_code == 200:
                    if time.time() < timeout_start + timeout:
                        existe = 'O site entrou ao CSV filtrado'
                        sitesfiltrados.append(url)
                        writer.writerow([url])
                    else:
                        print("Timeout: O site demorou muito para responder.")
                    
                elif request.status_code == 403:
                    print("Erro Acesso ao site bloqueado")
                    if time.time() < timeout_start + timeout:
                        existe = 'O site não entrou ao CSV filtrado'
                    else:
                        print("Timeout: O site demorou muito para responder.")
                        
                else:
                    if time.time() < timeout_start + timeout:
                        existe = 'O site não entrou ao CSV filtrado'
                    else:
                        print("Timeout: O site demorou muito para responder.")

            except:
                    if time.time() < timeout_start + timeout:
                        existe = 'O site não entrou ao CSV filtrado'
                    else:
                        print("Timeout: O site demorou muito para responder.")

            print(existe)
            print(" ")
            x=x+1
            break


print("Verificação de URLs finalizadas, iniciando criação do arquivo...")
time.sleep(5)
print("A verificação foi finalizada, foram adicionados", len(sitesfiltrados),"de",len(rawsites),"sites.")
print("Iniciando o crawler dos sites filtrados")
os.system("scrapy runspider crawler/crawler.py")

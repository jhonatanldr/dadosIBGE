import pyodbc
import requests
import json
from unicodedata import normalize

# Nova Sessão no Banco de Dados (SQL Server)
server = 'localhost'
database = 'TESTE'
username = 'python'
password = 'python'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()

# Busca das Mesorregiões dos Estados do Brasil na API do IBGE
request = requests.get(
    "https://servicodados.ibge.gov.br/api/v1/localidades/mesorregioes")
obj = json.loads(request.content)
for meso in obj:
    uf = meso['UF']
    ##################################################################
    meso_id = meso['id']
    meso_nome = normalize('NFKD', (meso['nome'])).encode('ASCII', 'ignore').decode('ASCII')
    meso_uf = uf['id']
    cursor.execute("INSERT INTO TESTE.[dbo].[mesorregioes] (id, nome, estado) VALUES (?, ?, ?)", meso_id, meso_nome, meso_uf)
    cursor.commit()

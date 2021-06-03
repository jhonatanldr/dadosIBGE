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

# Busca dos Municípios dos Estados do Brasil na API do IBGE
request = requests.get(
    "https://servicodados.ibge.gov.br/api/v1/localidades/municipios")
obj = json.loads(request.content)
for municipio in obj:
    ##################################################################
    regiao = municipio['regiao-imediata']
    regiaoI = regiao['regiao-intermediaria']
    regiaoU = regiaoI['UF']
    meso = municipio['microrregiao']
    mesoA = meso['mesorregiao']
    ##################################################################
    municipio_id = municipio['id']
    municipio_nome = normalize('NFKD', (municipio['nome'])).encode('ASCII', 'ignore').decode('ASCII')
    municipio_uf = regiaoU['id']
    municipio_meso = mesoA['id']
    cursor.execute("INSERT INTO TESTE.[dbo].[municipios] (id, nome, estado, mesorregiao) VALUES (?, ?, ?, ?)", municipio_id, municipio_nome, municipio_uf, municipio_meso)
    cursor.commit()
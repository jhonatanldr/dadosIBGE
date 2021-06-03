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

# Busca dos dados de Estados do Brasil na API do IBGE
request = requests.get(
    "https://servicodados.ibge.gov.br/api/v1/localidades/estados")
obj = json.loads(request.content)
for estado in obj:
    regiao = estado['regiao']
    estado_id = estado['id']
    estado_sigla = estado['sigla']
    estado_nome = normalize('NFKD', (estado['nome'])).encode('ASCII', 'ignore').decode('ASCII')
    estado_regiao = regiao['id']
    cursor.execute("INSERT INTO TESTE.[dbo].[ESTADOS] (id, sigla, nome, regiao) VALUES (?, ?, ?, ?)", estado_id, estado_sigla, estado_nome, estado_regiao)
    cursor.commit()
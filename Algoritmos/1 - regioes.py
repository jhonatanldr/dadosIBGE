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

# Busca das Regiões do Brasil na API do IBGE
request = requests.get(
    "https://servicodados.ibge.gov.br/api/v1/localidades/regioes")
obj = json.loads(request.content)
for regiao in obj:
    regiao_id = regiao['id']
    regiao_sigla = regiao['sigla']
    regiao_nome = normalize('NFKD', (regiao['nome'])).encode('ASCII', 'ignore').decode('ASCII')
    cursor.execute("INSERT INTO TESTE.[dbo].[REGIOES] (id, sigla, nome) VALUES (?, ?, ?)", regiao_id, regiao_sigla, regiao_nome)
    cursor.commit()
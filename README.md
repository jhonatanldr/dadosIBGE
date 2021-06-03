# dadosIBGE
Algoritmos em Python para extração de dados da API do IBGE e importação em Banco de Dados SQL Server (pyodbc)

Algoritmos criados com a finalidade de extração de dados das Regiões, Estados, Mesorregiões e Municípios do Brasil para inserção em Bancos de Dados.
O Banco de dados utilizado neste exemplo é o SQL Server, mas pode ser alterado para outros bancos, após a troca do driver no conector pyodbc e dos dados de acesso ao banco de dados de destino.

Segue abaixo algumas instruções para o correto funcionamento dos algoritmos.

Primeiramente deve-se criar as tabelas no Banco de Dados. O diretório "Scripts_das_Tabelas" já possui os arquivos os comandos para a criação das tabelas e dos campos. Para melhor utilização, recomendo a criação das tabelas na seguinte ordem:
1 - Regiões.sql
2 - Estados.sql
3 - Mesorregião.sql
4 - Municípios.sql

No diretório Algoritmos, possui os algoritmos em python para utilização. Para melhor extração dos dados da API do IBGE e inserção dos dados nas tabelas, recomento utilizar os algoritmos na seguinte ordem:
1 - regiões.py
2 - estados.py
3 - mesorregião.py
4 - municípios.py

Essa ordem é sugerida devido as Constraints que as tabelas possuem entre si.

Para mais detalhes sobre a api do IBGE, acesse o site: https://servicodados.ibge.gov.br/api/docs/localidades#api-_

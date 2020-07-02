import json

from pymongo import MongoClient

# Criar instância mongod
client = MongoClient()

# Obter a database dcwikia
db = client['dcwikia']

# Obter a collection linkPersonagens
link_personagens = db['linkPersonagens']

# Ler arquivo json
arquivo_Json = open('dadosDcWikia.json', 'r')

# Armazenar os dados do arquivo json no dicionário dados
dados_Json = json.load(arquivo_Json)

# Lista com todos os dados de cada personagem
personagens = dados_Json['personagens']

# Inserir em massa todos os links dos personagens
result = link_personagens.insert_many(personagens)

# Inserir as ids dos links dos personagens
ids_link_personagens = result.inserted_ids

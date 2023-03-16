"""
    Engenharia de dados - Trabalho 2
    By: João Goulart
"""

import pymongo
from mongoengine import *

# Definindo cliente mongo e instanciando banco
client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@eng-dados-1.dawrqwk.mongodb.net/?retryWrites=true&w=majority")
db = client['eng-dados-1']

# Conectando mongoengine
connect(host="mongodb+srv://mongodb:mongodb@eng-dados-1.dawrqwk.mongodb.net/?retryWrites=true&w=majority")



# Definindo coleções do banco


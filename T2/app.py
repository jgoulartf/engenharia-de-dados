"""
    --------------------------------------------------------
    Engenharia de dados - Trabalho 2
    Implementação de um banco de dados multidimensional.
    --------------------------------------------------------
    Made with: Python, MongoDB e mongoengine
    By: João Goulart - 16/03/2023
    --------------------------------------------------------
"""

from mongoengine import *
from lib import entrada_dados, insere_dados

DB_HOST = "mongodb+srv://mongodb:mongodb@eng-dados-1.dawrqwk.mongodb.net/?retryWrites=true&w=majority"

def main():
    try:
        # Definindo cliente mongo e instanciando banco
        # client = pymongo.MongoClient(DB_HOST)
        # db = client.get_database(name="eng-dados-1")
        # Conectando mongoengine
        connect(host=DB_HOST)
        print("Conectado ao banco!")
    except Exception as e:
        print(e)

    # Ler dados a partir do teclado
    entrada = entrada_dados()

    # Insere entrada no banco
    insere_dados(entrada)


main()

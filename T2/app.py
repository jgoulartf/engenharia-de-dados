"""
    --------------------------------------------------------
                Engenharia de dados - Trabalho 2
    --------------------------------------------------------
    Implementação de um banco de dados multidimensional.
    --------------------------------------------------------
    Made with: Python, MongoDB e mongoengine
    By: João Goulart - 16/03/2023
    --------------------------------------------------------
"""

from lib import *
from pymongo import *
from mongoengine import *

DB_HOST = "mongodb+srv://mongodb:mongodb@eng-dados-1.dawrqwk.mongodb.net/?retryWrites=true&w=majority"


def main():
    db = conexao_db()
    fornecedor = db['fornecedor']

    # Exibe menu de interação
    while True:
        try:
            dados, funcionou = menu()
        except Exception as e:
            print(e)

    """
    for documento in fornecedor.find({}):
        print(documento)
    """


main()

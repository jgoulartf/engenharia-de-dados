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

DB_HOST = "mongodb+srv://mongodb:mongodb@eng-dados-1.dawrqwk.mongodb.net/?retryWrites=true&w=majority"

def main():
    conexao_db()
    # Exibe menu de interação
    while True:
        try:
            dados, funcionou = menu()

        except Exception as e:
            print(e)

main()

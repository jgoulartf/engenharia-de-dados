import datetime

from models import *
from models.Cliente import Cliente
from models.Fornecedor import Fornecedor
from models.Medicamento import Medicamento
from models.Venda import Venda

def entrada_dados():
    fornecedor = ler_fornecedor()
    cliente = ler_cliente()
    medicamento = ler_medicamento()
    venda = ler_venda()

    return [fornecedor, cliente, medicamento, venda]

def insere_dados(dados):
    try:
        for dado in dados:
            dado.save()
        print("Dados inseridos com sucesso")
    except Exception as e:
        print(e)

def ler_fornecedor():
    print("Inserindo um fornecedor...")

    print("Nome - ")
    nome = str(input())

    print("Endereço - ")
    endereco = str(input())

    print("Telefone - ")
    telefone = str(input())

    fornecedor = Fornecedor(nome=nome, endereco=endereco, telefone=telefone)

    return fornecedor

def ler_cliente():
    print("Inserindo um cliente...")

    print("Nome")
    nome = str(input())

    print("Endereço")
    endereco = str(input())

    print("Telefone")
    telefone = str(input())

    cliente = Cliente(nome=nome, endereco=endereco, telefone=telefone)

    return cliente

def ler_medicamento():
    print("Inserindo um medicamento...")

    print("Nome do fornecedor")
    id_fornecedor = str(input())

    print("Nome do medicamento")
    nome = str(input())

    print("Descrição")
    descricao = str(input())

    print("Valor")
    valor = float(input())

    cliente = Medicamento(id_fornecedor=id_fornecedor, nome=nome, descricao=descricao, valor=valor)

    return cliente

def ler_venda():
    print("Inserindo uma venda")
    print("Nome do cliente")
    id_cliente = str(input())

    print("Nome do medicamento")
    id_medicamento = str(input())

    print("Quantidade vendida")
    quantidade = float(input())

    data = datetime.date.today()

    venda = Venda(id_cliente=id_cliente, id_medicamento=id_medicamento, quantidade=quantidade, data=data)

    return venda

# TODO
"""
def gera_dimensoes():

def gera_fato():
"""

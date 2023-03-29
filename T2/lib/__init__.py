import datetime
from mongoengine import *
import pymongo as pymongo

from models.Cliente import Cliente
from models.DimensaoPedidos import DimensaoPedidos
from models.DimensaoVendas import DimensaoVendas
from models.Fato import Fato
from models.Fornecedor import Fornecedor
from models.Medicamento import Medicamento
from models.Venda import Venda

DB_HOST = "mongodb+srv://mongodb:mongodb@eng-dados-1.dawrqwk.mongodb.net/?retryWrites=true&w=majority"


def menu():
    print("------------MENU------------")
    print("1 - Popular banco")
    print("2 - Atualizar fato/dimensão")

    res = int(input())

    if res == 1:
        populacao = entrada_dados()
        # Insere entrada no banco
        insere_dados(populacao)
        return res, True
    elif res == 2:
        #gera_dimensoes()
        gera_fato()

    return res, False


def entrada_dados():
    fornecedor = ler_fornecedor()
    cliente = ler_cliente()
    medicamento = ler_medicamento()
    venda = ler_venda()

    return [fornecedor, cliente, medicamento, venda]


def insere_dados(dados):
    try:
        for dado in dados:
            print(dado)
            dado.save()
            # atualiza_fato()
        print("Dados inseridos com sucesso")
        print(dados)
        # atualiza_dimensoes(dados)
    except Exception as e:
        print(e)


def conexao_db():
    try:
        # Definindo cliente mongo e instanciando banco
        client = pymongo.MongoClient(DB_HOST)
        db = client["test"]
        # Conectando mongoengine
        connect(host=DB_HOST)
        return db
    except Exception as e:
        print("Erro ao tentar conectar com o banco...")
        print(e)


def dropa_banco():
    try:
        # Definindo cliente mongo e instanciando banco
        # client = pymongo.MongoClient(DB_HOST)
        # db = client.get_database(name="eng-dados-1")
        # Conectando mongoengine
        connect(host=DB_HOST)
        print("Conectado ao banco!")
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
def gera_dimensoes():
    total_vendas = 0
    try:
        db = conexao_db()
        fornecedores = db['fornecedor'].find()
        clientes = db['cliente'].find()
        medicamentos = db['medicamento'].find()
        vendas = db['venda'].find()

    except Exception as e:
        print(e)

    for venda in vendas:
        # print(venda['quantidade'])
        total_vendas = total_vendas + venda['quantidade']

    dimensao_vendas = DimensaoVendas(total_vendas=total_vendas)
    dimensao_vendas.save()

    dimensao_pedidos = DimensaoPedidos(id_fornecedor="João", id_medicamento="vacina", total_pedidos=20, data=datetime.date.today())
    dimensao_pedidos.save()


# TODO
def gera_fato():
    fato = Fato(
        id_dim_vendas='64242e7956e5c0feab6ff0d0',
        id_dim_pedidos='64242e7a56e5c0feab6ff0d1',
        quantidade_medicamentos_vendidos=50,
        valor_medio_medicamento_vendido=120,
        total_medicamento_pedidos=60,
        total_medicamento_pedidos_fornecedor=10,
        total_pedidos_mes=500,
    )
    fato.save()

from mongoengine import *

class Fornecedor(Document):
    nome = StringField()
    endereco = StringField()
    telefone = StringField()
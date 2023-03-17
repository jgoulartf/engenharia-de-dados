from mongoengine import *

class Fornecedor(Document):
    nome = StringField(primary_key=True)
    endereco = StringField()
    telefone = StringField()
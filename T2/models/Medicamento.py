from mongoengine import *

from models.Fornecedor import Fornecedor


class Medicamento(Document):
    id_fornecedor = ReferenceField(Fornecedor)
    nome = StringField()
    descricao = StringField()
    valor = FloatField()

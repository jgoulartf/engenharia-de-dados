from mongoengine import *

from models.Fornecedor import Fornecedor


class Medicamento(Document):
    id_fornecedor = ReferenceField(Fornecedor)
    nome = StringField(primary_key=True)
    descricao = StringField()
    valor = FloatField()

from mongoengine import *

from models import Fornecedor, Medicamento


class DimensaoPedidos(Document):
    id_fornecedor = ReferenceField(Fornecedor)
    id_medicamento = ReferenceField(Medicamento)
    data = DateField()

from mongoengine import *

from models.Fornecedor import Fornecedor
from models.Medicamento import Medicamento


class DimensaoPedidos(Document):
    id_fornecedor = ReferenceField(Fornecedor)
    id_medicamento = ReferenceField(Medicamento)
    total_pedidos = FloatField(min_value=0)
    data = DateField()

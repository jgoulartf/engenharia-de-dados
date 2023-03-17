from mongoengine import *

from models.Medicamento import Medicamento
from models.Cliente import Cliente


class Venda(Document):
    id_cliente = ReferenceField(Cliente)
    id_medicamento = ReferenceField(Medicamento)
    quantidade = FloatField(min_value=0)
    data = DateField()
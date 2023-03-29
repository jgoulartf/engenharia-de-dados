from mongoengine import *

from models.DimensaoVendas import DimensaoVendas
from models.DimensaoPedidos import DimensaoPedidos

class Fato(Document):
    id_dim_vendas = ReferenceField(DimensaoVendas)
    id_dim_pedidos = ReferenceField(DimensaoPedidos)
    quantidade_medicamentos_vendidos = FloatField(min_value=0)
    valor_medio_medicamento_vendido = FloatField(min_value=0)
    total_medicamento_pedidos = FloatField(min_value=0)
    total_medicamento_pedidos_fornecedor = FloatField(min_value=0)
    total_pedidos_mes = FloatField(min_value=0)

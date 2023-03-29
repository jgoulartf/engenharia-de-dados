from mongoengine import *

from models.Venda import Venda
class DimensaoVendas(Document):
    id_vendas = ReferenceField(Venda)
    total_vendas = FloatField(min_value=0)

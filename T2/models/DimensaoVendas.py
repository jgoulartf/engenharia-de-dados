from mongoengine import *

from models import Venda
class DimensaoVendas(Document):
    id_vendas = ReferenceField(Venda)
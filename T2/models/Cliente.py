from mongoengine import *

class Cliente(Document):
    nome = StringField(primary_key=True)
    endereco = StringField()
    telefone = StringField()
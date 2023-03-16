from mongoengine import *

class Cliente(Document):
    nome = StringField()
    endereco = StringField()
    telefone = StringField()
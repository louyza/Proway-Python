from model.framework import Framework
from model.db import Db
from model.linguagem_squad import Linguagem

class Programador:
    def __init__(self, nome, framework: Framework = None, db: Db = None, linguagem: Linguagem = None,
                 id_db=None, id_framework=None, id_linguagem=None, id=None):
        self.nome = nome
        self.linguagem = linguagem
        self.framework = framework
        self.db = db
        self.id_db = id_db
        self.id_framework = id_framework
        self.id_linguagem = id_linguagem
        self.id = id

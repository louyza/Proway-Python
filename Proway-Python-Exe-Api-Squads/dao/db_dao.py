
"""
from dao.base_dao import BaseDao
from model.db import Db

class DbDao(BaseDao):
    def listar(self):
        lista = []
        comando_sql_listar = 'SELECT db, id FROM banco_de_dados'
        todos = super().listar(comando_sql_listar)
        for l in todos:
            model_db = Db(l[0],l[1])
            lista.append(model_db)
        return lista
"""

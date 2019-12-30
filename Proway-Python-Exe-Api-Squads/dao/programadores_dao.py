from model.programador import Programador
from model.linguagem_squad import Linguagem
from model.framework import Framework
from model.db import Db
from dao.base_dao import BaseDao
import sys
sys.path.append("")


class ProgramadorDao(BaseDao):

    def inserir(self, programador: Programador):
        comando_sql_insert = f"""
                                INSERT INTO programadores (nome, id_db, id_framework, id_linguagem)
                                VALUES ('{programador.nome}', {programador.id_db},
                                {programador.id_framework}, {programador.id_linguagem})
                            """
        print(programador.__dict__)
        return super().inserir(comando_sql_insert)

    def alterar(self, programador: Programador):
        comando_sql_alterar = f"""
                                UPDATE programadores
                                SET nome = '{programador.nome}', id_db = {programador.id_db},
                                id_framework = {programador.id_framework}, id_linguagem = {programador.id_linguagem}
                                WHERE id = {programador.id}
                            """
        super().alterar(comando_sql_alterar)

    def deletar(self, id: int):
        comando_sql_deletar = f"""
                                DELETE FROM programadores
                                WHERE id = {id}
                            """
        super().alterar(comando_sql_deletar)
        return ('Você deletou o dado!')

    def listar(self):
        lista = []
        comando_sql_listar = """
                                SELECT 
                                p.nome,f.framework, f.id, bd.db, bd.id, 
                                l.linguagem, l.id
                                FROM programadores p 
                                JOIN banco_de_dados as bd JOIN linguagem_squad as l JOIN framework as f
                                ON p.id_db = bd.id AND p.id_framework = f.id AND p.id_linguagem = l.id

                            """
        todos = super().listar(comando_sql_listar)
        for l in todos:
            framework = Framework(l[1], l[2])
            db = Db(l[3], l[4])
            linguagem = Linguagem(l[5], l[6])
            model_programador = Programador(
                l[0], framework.__dict__, db.__dict__, linguagem.__dict__)
            lista.append(model_programador.__dict__)
        return lista

    def buscar_por_id(self, id: int):
        comando_sql_buscar_id = f"""
                                SELECT 
                                p.nome,f.framework, f.id, bd.db, bd.id, 
                                l.linguagem, l.id
                                FROM programadores p 
                                JOIN banco_de_dados as bd JOIN linguagem_squad as l JOIN framework as f
                                ON p.id_db = bd.id AND p.id_framework = f.id AND p.id_linguagem = l.id
                                WHERE p.id = {id}
                            """
        tupla = super().buscar_por_id(comando_sql_buscar_id)
        framework = Framework(tupla[1], tupla[2])
        db = Db(tupla[3], tupla[4])
        linguagem = Linguagem(tupla[5], tupla[6])
        model_programador = Programador(
            tupla[0], framework.__dict__, db.__dict__, linguagem.__dict__)
        return model_programador.__dict__

    def existe_nome(self, nome):
        comando_sql_buscar_id = f"""
                                    SELECT * FROM programadores WHERE nome LIKE '%{nome}%' LIMIT 1
                                """
        verific = super().buscar_por_id(comando_sql_buscar_id)
        if verific:
            return True
        else:
            return False

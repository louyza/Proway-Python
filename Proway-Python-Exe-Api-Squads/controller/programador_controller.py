from flask_restful import Resource
from flask import request
from model.programador import Programador
from dao.programadores_dao import ProgramadorDao


class ProgramadoresController(Resource):
    def __init__(self):
        self.dao = ProgramadorDao()

    def get(self, id=None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar()

    def post(self):
        nome = request.json['nome']
        id_db = request.json['id_db']
        id_framework = request.json['id_framework']
        id_linguagem = request.json['id_linguagem']

        if self.dao.existe_nome(nome):
            return "Usuário já existe!"

        if len(self.dao.listar()) == 3:
            return "Lista completa!"

        if nome.lower() == 'nicole' and id_db == 1 and id_framework == 1 and id_linguagem == 1:

            programador = Programador(
                nome.lower(), id_framework=id_framework, id_db=id_db, id_linguagem=id_linguagem)
            programador_id = self.dao.inserir(programador)
            programador = self.dao.buscar_por_id(programador_id)
            return programador

        elif nome.lower() == 'mateus' and id_db == 2 and id_framework == 2 and id_linguagem == 2:
            programador = Programador(
                nome.lower(), id_framework=id_framework, id_db=id_db, id_linguagem=id_linguagem)
            programador_id = self.dao.inserir(programador)
            programador = self.dao.buscar_por_id(programador_id)
            return programador

        elif nome.lower() == 'tiago' and id_db == 3 and id_framework == 3 and id_linguagem == 3:
            programador = Programador(
                nome.lower(), id_framework=id_framework, id_db=id_db, id_linguagem=id_linguagem)
            programador_id = self.dao.inserir(programador)
            programador = self.dao.buscar_por_id(programador_id)
            return programador

        else:
            return 'Combinação Inválida'

    def put(self, id):
        id_body = request.json['id']
        nome = request.json['nome']
        id_db = request.json['id_db']
        id_framework = request.json['id_framework']
        id_linguagem = request.json['id_linguagem']

        if id_body != id:
            return 'Ids de rota e body diferentes, seu tatu!'
        programador = Programador(
            nome, id_db=id_db, id_framework=id_framework, id_linguagem=id_linguagem, id=id)
        self.dao.alterar(programador)
        programador = self.dao.buscar_por_id(id)
        return programador

    def delete(self, id):
        programador = self.dao.buscar_por_id(id)
        self.dao.deletar(id)
        return f'{programador["nome"]} deletado'

#---- API

from flask import Flask
from flask_restful import Api
from controller.programador_controller import ProgramadoresController

app = Flask(__name__)
api = Api(app)

api.add_resource(ProgramadoresController,
                 '/api/programadores', endpoint='programadores')
api.add_resource(ProgramadoresController,
                 '/api/programadores/<int:id>', endpoint='programador')

app.run(debug=True)

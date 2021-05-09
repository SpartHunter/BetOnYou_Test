# app/__init__.py

from flask_restx import Api
from flask import Blueprint

from .src.controller.player_controller import api as player_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API WITH JWT',
          version='1.0',
          description='A Flask RESTX API For My Candidature Test'
          )

api.add_namespace(player_ns, path='/player')

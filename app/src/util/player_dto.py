from flask_restx import Namespace, fields


class PlayerDto:

    api = Namespace('player', description='player related all operation')

    player = api.model('player', {
        'firstname': fields.String(required=True, description='Player firstname'),
        'lastname': fields.String(required=True, description='Player lastname'),
        'email': fields.String(required=True, description='Player email'),
        'username': fields.String(required=True, description='Player username'),
        'gamename1': fields.String(required=False, description='Player first game'),
        'gamename2': fields.String(required=False, description='Player second game'),
        'active': fields.Boolean(required=True, description='Acount player status'),
        'password': fields.String(require=True, description='Player acount password')
    })


import json

from flask import request
from flask_restx import Resource

from ..util.player_dto import PlayerDto
from ..service.player_service import addPlayer, getAllPlayer, getPlayer, putPlayer, DeletePlayer

api = PlayerDto.api
_player = PlayerDto.player


@api.route('/')
class Player(Resource):

    @api.response(200, 'All Player received.')
    @api.response(409, 'Error in receive all player.')
    @api.doc('list_of_registered_players')
    def get(self):
        """List all registered players"""
        players = getAllPlayer()
        return players

    @api.response(201, 'Player successfully created.')
    @api.response(409, 'Player fail created.')
    @api.doc('create a new player')
    @api.expect(_player, validate=True)
    def post(self):
        """Creates a new player """
        data = request.get_json()
        player = addPlayer(data=data)
        return player


@api.route('/<public_id>')
@api.param('public_id', 'The player identifier')
class PlayerResource(Resource):
    @api.doc('Get a player')
    @api.response(200, 'Player success found.')
    @api.response(404, 'Player fail found.')
    def get(self, public_id):
        """get a player given its identifier"""
        player = getPlayer(public_id)
        if not player:
            api.abort(404)
        else:
            return player

    @api.doc('Put a player')
    @api.response(200, 'Player success found.')
    @api.response(404, 'Player fail found.')
    @api.expect(_player, validate=True)
    def put(self, public_id):
        """Get a player given its identifier and put update data"""
        data = request.get_json()
        update_player = putPlayer(public_id, data)
        if not update_player:
            api.abort(404)
        else:
            return update_player

    @api.doc('Delete a player')
    @api.response(200, 'Player success found.')
    @api.response(404, 'Player fail found.')
    def delete(self, public_id):
        """get a player given its identifier and delete data"""
        delete_player = DeletePlayer(public_id)
        if not delete_player:
            api.abort(404)
        else:
            return delete_player

from app.src import db
from app.src.model.player_model import Player
import json


def addPlayer(data):
    user = Player.query.filter_by(email=data['email']).first()

    if not user:

        new_player = Player(
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            email=data.get('email'),
            username=data.get('username'),
            gamename1=data.get('gamename1'),
            gamename2=data.get('gamename2'),
            active=data.get('active'),
            password=data.get('password'),
        )

        db.session.add(new_player)

        db.session.commit()

        jsonplayer = {
            'firstname': new_player.firstname,
            'lastname': new_player.lastname,
            'email': new_player.email,
            'username': new_player.username,
            'gamename1': new_player.gamename1,
            'gamename2': new_player.gamename2,
            'active': new_player.active,
            'password': new_player.password
        }

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'player': jsonplayer
        }

        return response_object, 201

    else:

        response_object = {
            'status': 'fail',
            'message': 'Player already exists. Please Log in.',
        }

        return response_object, 409


def getAllPlayer():
    players = Player.query.all()

    if players:

        listplayer = []

        for element in players:
            jsonelement = {
                'firstname': element.firstname,
                'lastname': element.lastname,
                'email': element.email,
                'username': element.username,
                'gamename1': element.gamename1,
                'gamename2': element.gamename2,
                'active': element.active,
                'password': element.password
            }

            listplayer.append(jsonelement)

        response_object = {
            'status': 'success',
            'message': 'Success receive list of all player',
            'players': listplayer
        }

        return response_object, 200

    else:

        response_object = {
            'status': 'fail',
            'message': 'Receive empty Player list or other data',
        }

        return response_object, 409


def getPlayer(public_id):
    player = Player.query.filter_by(id=public_id).first()

    if player:

        jsonplayer = {
            'firstname': player.firstname,
            'lastname': player.lastname,
            'email': player.email,
            'username': player.username,
            'gamename1': player.gamename1,
            'gamename2': player.gamename2,
            'active': player.active,
            'password': player.password
        }

        response_object = {
            'status': 'success',
            'message': 'Success receive player data',
            'player': jsonplayer
        }

        return response_object, 200

    else:

        response_object = {
            'status': 'fail',
            'message': 'Receive empty Player list or other data',
        }

        return response_object, 404


def putPlayer(public_id, data):

    player = Player.query.filter_by(id=public_id).first()

    print('************ddd************')
    print(data)
    print('***********ddd*************')

    print('************ppp************')
    print(player)
    print('**********ppp**************')
    if player:

        print('************ppp************')
        player.firstname = data.get('firstname')
        player.lastname = data.get('lastname')
        player.email = data.get('email')
        player.username = data.get('username')
        player.gamename1 = data.get('gamename1')
        player.gamename2 = data.get('gamename2')
        player.active = data.get('active')
        player.password = data.get('password')

        print(player)
        print('**********ppp**************')

        db.session.commit()

        jsonplayer = {
            'firstname': player.firstname,
            'lastname': player.lastname,
            'email': player.email,
            'username': player.username,
            'gamename1': player.gamename1,
            'gamename2': player.gamename2,
            'active': player.active,
            'password': player.password
        }

        response_object = {
            'status': 'success',
            'message': 'Success update player id {}'.format(public_id),
            'player': jsonplayer
        }

        return response_object, 200

    else:

        response_object = {
            'status': 'fail',
            'message': 'Receive empty Player list or other data',
        }

        return response_object, 404


def DeletePlayer(public_id):

    player = Player.query.filter_by(id=public_id).first()

    if player:

        db.session.delete(player)

        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'Success deleted player id : {}'.format(public_id),
        }

        return response_object, 200

    else:

        response_object = {
            'status': 'fail',
            'message': 'failed delete player id : {}'.format(public_id),
        }

        return response_object, 404

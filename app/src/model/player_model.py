from .. import db


class Player(db.Model):
    """ player Model for storing Player related details """
    __tablename__ = "Player"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(25), nullable=False)
    lastname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(25), nullable=False, unique=True)
    gamename1 = db.Column(db.String(25), nullable=True)
    gamename2 = db.Column(db.String(25), nullable=True)
    active = db.Column(db.Boolean(), nullable=False, default=False)
    password = db.Column(db.String(100))

    def __repr__(self):
        return "<Player '{}'>".format(self.firstname)



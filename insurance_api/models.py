from passlib.hash import pbkdf2_sha256
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    ''' Model to represent User's login and personal
        data for insurance recommendations.
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    name = db.Column(db.String(80), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    children = db.Column(db.Boolean, nullable=True)
    num_children = db.Column(db.Integer, nullable=True)
    occupation = db.Column(db.String(80), nullable=True)
    occupation_type = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=True)

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_user(cls, username) -> str:
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def pw_hash(password) -> str:
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash) -> str:
        return pbkdf2_sha256.verify(password, hash)

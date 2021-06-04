from api.utils.database import db
from api.utils.schema import ma
from marshmallow import fields
from passlib.hash import pbkdf2_sha256 as sha256


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), nullable=False)
    hash_password = db.Column(db.String(140))
    avatar = db.Column(db.String(20))
    posts = db.relationship('Post', backref='user')

    def __init__(self, *args, **kwargs):
        self.posts = []
        super(User, self).__init__(*args, **kwargs)

    @property
    def password(self):
        raise AttributeError('password is write only field')

    @password.setter
    def password(self, password):
        self.hash_password = sha256.hash(password)

    def check_password(self, password):
        return sha256.verify(password, self.hash_password)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    photo = db.Column(db.String(20), nullable=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    likes = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class PostLikes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    like_time = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, *args, **kwargs):
        super(PostLikes, self).__init__(*args, **kwargs)


class LoginHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    last_time_login = db.Column(db.DateTime)


class RequestHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    request_time = db.Column(db.DateTime)
    description = db.Column(db.String(40))


class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Post

    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    user_id = fields.Integer()
    created = fields.DateTime()
    likes = fields.Integer()


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    avatar = fields.String()

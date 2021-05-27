from api import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(40))
    posts = db.relationship('Post', backref='User', cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        self.posts = []
        super(User, self).__init__(args, kwargs)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(250))
    created = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(args, kwargs)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


# class PostSchema(ModelSchema):
#     class Meta(ModelSchema.Meta):
#         model = Post
#         sqla_session = db.session
#
#     id = fields.Number(dump_only=True)
#     title = fields.String(required=True)
#     body = fields.String(required=True)
#     user_id = fields.Number()
#
#
# class UserSchema(ModelSchema):
#     class Meta(ModelSchema.Meta):
#         model = User
#         sqla_session = db.session
#
#     id = fields.Integer(dump_only=True)
#     first_name = fields.String(required=True)
#     last_name = fields.String(required=True)
#     created = fields.String(dump_only=True)
#     posts = fields.Nested(PostSchema, many=True,
#                           only=['title', 'body', 'id'])
#
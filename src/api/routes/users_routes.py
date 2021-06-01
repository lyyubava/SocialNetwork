from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.models import User, UserSchema
from api.models.models import Post, PostSchema
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

user_routes = Blueprint("user_routes", __name__)


@user_routes.route('/login', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        current_user = User.query.filter_by(username=data['username']).first()
        if not current_user:
            return response_with(resp.SERVER_ERROR_404)
        if current_user.check_password(data['password']):
            access_token = create_access_token(identity=data['username'])
            return response_with(resp.SUCCESS_201, value={'message': 'Logged in as {}'.format(current_user.username),
                                                          "access_token": access_token})
        else:
            return response_with(resp.UNAUTHORIZED_401)

    except Exception as e:
        print(e)
        return response_with(resp.UNAUTHORIZED_401)


@user_routes.route('/', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user_schema = UserSchema()

        user = User(**(user_schema.load(data)))
        user.create()
        return response_with(resp.SUCCESS_201)

    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@user_routes.route('/<string:username>', methods=['GET'])
def get_user(username):
    fetch = User.query.filter_by(username=username).first()
    user_schema = UserSchema()
    user = user_schema.dump(fetch)
    # user = user_schema.dump(fetch)
    # print(user)
    return response_with(resp.SUCCESS_200, value={"user": user})


@user_routes.route('/<string:username>/posts', methods=['GET'])
def display_posts(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422)
    posts = user.posts
    post_schema = PostSchema()
    posts_list = list()
    for post in posts:
        dumped_post = post_schema.dump(post)
        posts_list.append(dumped_post)
    return response_with(resp.SUCCESS_200, value={"post": posts_list})


@user_routes.route('/<string:username>/create_post', methods=['POST'])
def create_post(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422)
    data = request.get_json()
    post_schema = PostSchema()
    post = Post(**(post_schema.load(data)))
    user.posts.append(post)
    post.create()
    return response_with(resp.SUCCESS_201)




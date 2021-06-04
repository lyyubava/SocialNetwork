from flask import Blueprint
from flask import request, jsonify
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.models import User, UserSchema
from api.models.models import Post, PostSchema
from api.models.models import PostLikes
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.utils.database import db
from sqlalchemy import and_, func

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
@jwt_required()
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


@user_routes.route('/like.<action>', methods=['POST'])
def like_action(action):
    data = request.get_json()
    post_id = data["post_id"]
    user_id = data["user_id"]
    post = Post.query.filter_by(id=post_id).first()

    if not post:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422)

    if action == 'add':

        if PostLikes.query.filter_by(user_id=user_id, post_id=post_id).first() is None:
            if post.likes is None:
                post.likes = 1
            else:
                post.likes += 1
            # db.session.commit()
            post_like = PostLikes(user_id=user_id, post_id=post_id)

            db.session.add(post_like)
            db.session.commit()
            return response_with(resp.SUCCESS_201)

        return jsonify(mesaage="is already liked")

    elif action == 'delete':
        if PostLikes.query.filter_by(user_id=user_id, post_id=post_id).first() is not None:
            post.likes -= 1
            post_unlike = PostLikes.query.filter_by(user_id=user_id, post_id=post_id).first()
            db.session.delete(post_unlike)
            db.session.commit()

        else:
            return jsonify(mesaage="you cannot unlike post that you haven`t liked :) ")

    return response_with(resp.SUCCESS_201)


@user_routes.route('/analytics', methods=['POST'])
def get_analytics():
    returned_dict = dict()
    data = request.get_json()
    date_from = data['date_from']
    date_to = data['date_to']
    total = db.session.query(func.count(PostLikes.user_id),
                             func.date(PostLikes.like_time)).filter(and_(PostLikes.like_time >= date_from,
                                                                         PostLikes.like_time <= date_to)).group_by(func.date(PostLikes.like_time)).all()
    for amount, date in total:
        returned_dict[amount] = date

    return response_with(resp.SUCCESS_200, value={f"total amount of likes from {date_from} to {date_to}": returned_dict})


@user_routes.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()



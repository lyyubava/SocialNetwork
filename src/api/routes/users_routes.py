from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.models import User, UserSchema

user_routes = Blueprint("user_route", __name__)


@user_routes.route('/<string:username>', methods=['GET'])
def get_use(username):
    fetch = User.query.filter_by(username=username).first()

    user_schema = UserSchema()
    user = user_schema.dump(fetch)
    # user = user_schema.dump(fetch)
    # print(user)
    return response_with(resp.SUCCESS_200, value={"user": user})


@user_routes.route('/', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user_schema = UserSchema()

        user = User(**(user_schema.load(data)))
        user.create()
        print(user)
        return response_with(resp.SUCCESS_201)

    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
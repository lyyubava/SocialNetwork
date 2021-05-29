from api.utils.responses import response_with
import api.utils.responses as resp
import logging
from flask import Flask, jsonify
from api.config.config import Configuration
from api.utils.database import db
from api.routes.users_routes import user_routes
from api.utils.schema import ma
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(user_routes, url_prefix='/api/users')


@app.after_request
def add_header(response):
    return response


@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)


@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)


@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)


jwt = JWTManager(app)
db.init_app(app)
ma.init_app(app)

# with app.app_context():
#     app.app_context().pop()
#     app.app_context().push()
#     db.create_all()
#

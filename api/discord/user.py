from data.database import User, db_session
from flask import Blueprint, abort, jsonify, request

blueprint = Blueprint("user", __name__, url_prefix="/user")


@blueprint.route('<int:discord_id>', methods=["GET"])
def get_user(discord_id):
    sess = db_session.create_session()
    user = sess.query(User).filter(User.discord_id == discord_id).first()
    if user:
        return jsonify(user.to_dict())
    abort(404, "User Not Found")

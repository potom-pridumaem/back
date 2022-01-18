from data.database import Group, db_session
from flask import Blueprint, abort, jsonify, request

blueprint = Blueprint("group", __name__, url_prefix="/group")


@blueprint.route('<int:id>', methods=["GET"])
def get_group(id):
    sess = db_session.create_session()
    user = sess.query(Group).get(id)
    if user:
        return jsonify(user.to_dict())
    abort(404, "Group Not Found")

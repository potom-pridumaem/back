from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from data import db_session
from data import Group
from data import UserGroup as UG

blueprint = Blueprint('groups_api', __name__)


@blueprint.route('/api/group/<group_name>', methods=['POST'])
@jwt_required()
def register_group(group_name):
    Group.if_group_already_created(group_name)
    sess = db_session.create_session()
    user_id = get_jwt_identity()
    group = Group(
        name=group_name,
        admin_id=user_id
    )
    sess.add(group)
    sess.commit()
    user_group = UG(
        group_id=group.id,
        user_id=user_id
    )
    sess.add(user_group)
    sess.commit()
    return jsonify({'success': 'OK', "group_id": group.id}), 200


@blueprint.route('/api/group/<group_name>', methods=['PATCH'])
@jwt_required()
def update_group_name(group_name):
    user_id = int(get_jwt_identity())
    Group.if_group_not_found_by_name(group_name)
    Group.if_user_is_not_admin(group_name, user_id)
    req = request.get_json(force=True)
    sess = db_session.create_session()
    group = sess.query(Group).filter(Group.name == group_name)
    group.group_name = req['new_group_name']
    sess.commit()
    return jsonify({'success': 'OK'}), 200


import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.schema import ForeignKey
from flask import abort

from data.db_session import SqlAlchemyBase
from data import db_session
from  data.models.User_Group import UserGroup as UG


class User(SqlAlchemyBase, SerializerMixin):  # название модели
    __tablename__ = 'users'  # Название таблицы

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # поля таблицы
    name = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    vk_data = sqlalchemy.Column(sqlalchemy.Text)

    def if_user_not_found_by_id(user_id):
        sess = db_session.create_session()
        user = sess.query(User.id).filter(User.id == user_id).first()
        if not user:
            abort(404, 'User id not found')

    def if_user_not_found_by_name(user_name):
        sess = db_session.create_session()
        user = sess.query(User.id).filter(User.name == user_name).first()
        if not user:
            abort(404, 'User name not found')

    def if_user_not_found_by_group(group_id):
        sess = db_session.create_session()
        user = sess.query(UG.user_id).filter(UG.group_id == group_id).first()
        if not user:
            abort(404, 'User with this group_id name not found')

    def if_user_already_created(user_name):
        sess = db_session.create_session()
        user = sess.query(User.id).filter(User.name == user_name).first()
        if user:
            abort(403, 'User already created')
from data.database.db_session import SqlAlchemyBase
from sqlalchemy import Column, Enum, Integer
from sqlalchemy.schema import ForeignKey
from sqlalchemy_serializer import SerializerMixin

from ..types.role import RoleType


class Role(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "user"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("group.id"), primary_key=True)
    role = Column(Enum(RoleType))

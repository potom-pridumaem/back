from data.database.db_session import SqlAlchemyBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from sqlalchemy_serializer import SerializerMixin


class Group(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "user"

    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True, unique=True)
    name = Column(String)

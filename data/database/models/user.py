from data.database.db_session import SqlAlchemyBase
from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.schema import ForeignKey
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "user"

    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True, unique=True)
    name = Column(String)
    discord_id = Column(BigInteger)

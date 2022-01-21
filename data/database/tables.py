"""
Database models
"""
from sqlalchemy import BigInteger, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .engine import Base
from .types import RoleEnum


class User(Base):
    __tablename__ = "user"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True,
        index=True,
    )
    username = Column(String, nullable=False, unique=True, index=True)
    discord_id = Column(BigInteger, index=True)
    email = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    groups = relationship("UserGroup", back_populates="user")


class Group(Base):
    __tablename__ = "group"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True,
        index=True,
    )
    name = Column(String)
    users = relationship("UserGroup", back_populates="group")


class UserGroup(Base):
    __tablename__ = "user_group"

    user_id = Column(ForeignKey(User.id), primary_key=True)
    group_id = Column(ForeignKey(Group.id), primary_key=True)
    role = Column(Enum(RoleEnum), nullable=False)
    user = relationship("User", back_populates="groups")
    group = relationship("Group", back_populates="users")

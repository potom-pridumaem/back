import sqlalchemy.ext.declarative as dec
from config import envs
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

SqlAlchemyBase = dec.declarative_base()

some_engine = create_engine(envs.DATABASE_URL)

__factory = sessionmaker(bind=some_engine)

SqlAlchemyBase.metadata.create_all(some_engine)


def create_session() -> Session:
    global __factory
    return __factory()

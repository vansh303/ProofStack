from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_database_engine(database_url: str):
    return create_engine(
        database_url,
        pool_pre_ping = True,
    )

def create_session_factory(database_url: str):
    engine = create_database_engine(database_url)

    return sessionmaker(
        bind = engine,
        autoflash = False,
        autocommit=False,
    )
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DB_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DB_URL,connect_args={"check_same_thread":False}) 
# connect_args={"check_same_thread":False} --> tells multiple threads are used in case of sqlite

#NOTE:like a path or bridge btw the engine & base
sessionLocal = sessionmaker(autocommit=False,bind=engine)

#NOTE:for crating models
Base = declarative_base()
from sqlalchemy import create_engine  # setup database engine

from sqlalchemy.ext.declarative import declarative_base # database models

from sqlalchemy.orm import sessionmaker

DB_URL="mysql+pymysql://root:root@localhost/fastapi"

""" here established the connection with the engine echo 
logs(show in terminal) all sql statements"""

engine=create_engine(DB_URL,echo=True) 

"""sessionmaker is used to create new session objects 
bind=engine links session to the engine autocommit nd
autoflush ensure """

SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False) 

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('mysql+pymysql://root:root1@localhost/err')
DBSession = scoped_session(sessionmaker(bind = engine))
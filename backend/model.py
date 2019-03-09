from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect
from dbSetup import engine

Base = declarative_base()

class Item(Base):
    __tablename__ = 'rss_feed'
    id = Column(Integer, primary_key = True)
    title = Column(String(250), nullable = False)
    link = Column(String(250), nullable = False)
    description = Column(String(1000), nullable = False)
    published_date = Column(String(250), nullable = False)

    def addToDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

Base.metadata.create_all(engine)
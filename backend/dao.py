from model import Item
from dbSetup import DBSession

#Base.metadata.bind = engine

class Dao:
    def writeToDB(title, link, description, date):
        newEntry = Item(title = title, link = link, description = description, published_date = date)
        DBSession.add(newEntry)
        DBSession.commit()

    def queryFromDB():
        return DBSession.query(Item).order_by(Item.id.desc()).limit(50).all()







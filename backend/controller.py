from flask import Flask, jsonify
from service import *
from flask_cors import CORS
from cachetools import cached, TTLCache
from dbSetup import DBSession

app = Flask(__name__)
CORS(app)
cache = TTLCache(maxsize = 50, ttl = 300)


@app.route("/", methods=['GET'])
@cached(cache)
def getRSSFromDB():
    with app.app_context():
        serviceStatus = Service.getRSS()
        dbEntries = Dao.queryFromDB()
        if (serviceStatus == 200 and len(dbEntries) > 0):
            listToDict = []
            for dbEntry in dbEntries:
                listToDict.append(dbEntry.addToDict())
            return jsonify(listToDict)
        else:
            return '500'

@app.teardown_appcontext
def cleanup(resp_or_exc):
    DBSession.remove()

DEBUG = False
app.config.from_object(__name__)
if __name__ == '__main__':
    app.run()
import feedparser
from dao import *

class Service:
    def getRSS():
        rss = feedparser.parse("https://www.err.ee/rss")
        if (rss.status == 200):
            for rssItem in reversed(rss['items']):
                title = rssItem.title
                link = rssItem.link
                description = rssItem.description
                publishedDate = rssItem.published
                if Service.findNewRSS(rssItem) == True:
                    Dao.writeToDB(title, link, description, publishedDate)
        return rss.status

    def findNewRSS(rssItem):
        foundNewFeed = True
        dbEntries = Dao.queryFromDB()
        for dbEntry in dbEntries:
            if rssItem.title == dbEntry.title and rssItem.link == dbEntry.link:
                return False
        return foundNewFeed
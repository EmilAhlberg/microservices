# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import pymongo
import logging
from steamscraper.items import GameRawDataItem, SteamTopListItem
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
from steamscraper.items import SteamTopListItem,Game

class SteamscraperPipeline:

    def __init__(self):
        settings = get_project_settings()
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.validate_connection(connection, settings, db)
        self.gamedata_collection = db[settings['MONGODB_STEAMDATA_COLLECTION']]
        self.game_collection = db[settings['MONGODB_GAME_COLLECTION']]

    def validate_connection(self, connection, settings, db):
        dblist = connection.list_database_names()
        if settings['MONGODB_DB'] not in dblist:
            print("The database does not exists.")

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:

            print(item)

            if not self.game_collection.find_one({'gameTitle': item['gameTitle']}):
                #subset pattern, add entry if non-existing
                game = Game()
                game['gameTitle'] = item['gameTitle']
                game['developer'] = item['developer']
                game['publisher'] = item['publisher']
                game['steamData'] = []
                self.game_collection.insert(dict(game))

            steamTopListItem = SteamTopListItem()
            steamTopListItem['currentUsers'] = item['currentUsers']
            steamTopListItem['dailyPeakUsers'] = item['dailyPeakUsers']
            steamTopListItem['gameTitle'] = item['gameTitle']
            steamTopListItem['listRank'] = item['listRank']
            steamTopListItem['timestamp'] = item['timestamp']

            # insert into big collection
            self.gamedata_collection.insert(dict(steamTopListItem))
            # insert as a subset of latest data, on 'game'
            self.game_collection.find_one_and_update({'gameTitle': steamTopListItem['gameTitle']},
                {'$push': {'steamData': {'$each': [dict(steamTopListItem)], '$slice': -100}}}) #subset pattern of 100 samples
            logging.debug("Steam scraped item added to MongoDB database!")
        return item

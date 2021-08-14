# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class SteamTopListItem(Item):
    currentUsers = Field()
    dailyPeakUsers = Field()
    gameTitle = Field()
    listRank = Field()
    timestamp = Field()
    pass

# MongoDB  subset-pattern
class Game(Item):
    gameTitle = Field()
    developer = Field()
    publisher = Field()
    steamData = Field()
    pass

class GameRawDataItem(Item):
    developer = Field()
    publisher = Field()
    currentUsers = Field()
    dailyPeakUsers = Field()
    gameTitle = Field()
    listRank = Field()
    timestamp = Field()
    pass

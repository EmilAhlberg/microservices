import scrapy
import datetime
from steamscraper.items import SteamTopListItem, GameRawDataItem


class SteamSpider(scrapy.Spider):
    name = "steam"

    #start_urls = ['https://store.steampowered.com/stats/']

    def parse (self, response):

        detailStats = response.xpath('//*[@id="detailStats"]')
        gameOrganisationLinks =  detailStats.xpath('//*[@class="gameLink"]/@href')
        currentPlayers = detailStats.xpath('//*[@class="player_count_row"]/td[1]/span/text()')
        peakPlayers = detailStats.xpath('//*[@class="player_count_row"]/td[2]/span/text()')
        gameTitle = detailStats.xpath('//*[@class="player_count_row"]/td/a/text()')
        gamelink = detailStats.xpath('//*[@class="player_count_row"]/td/a/text()')

        for rank, (cp, pp, gt, link) in enumerate(zip(currentPlayers, peakPlayers, gameTitle, gameOrganisationLinks)):
            #item = SteamTopListItem()
            #item['listRank'] = rank
            #item['currentUsers'] = cp.get()
            #item['dailyPeakUsers'] = pp.get()
            #item['gameTitle'] = gt.get()

            yield scrapy.FormRequest(link.get(),
                    callback=self.fetchGameOrganisations,
                    meta={
                        'listRank': rank,
                        'currentUsers': cp.get(),
                        'dailyPeakUsers': pp.get(),
                        'gameTitle': gt.get()
                    })
            #yield from response.follow(link.get(), cookies={'birthtime': '0'}, #circumvent steam agecheck
            #        callback=self.callbackWithParam(self.parseGameData, "hej"))

    def fetchGameOrganisations(self, response):
        item = GameRawDataItem()
        a = response.xpath('//*[@id="developers_list"]/../..') #navigate via unique id --> parent
        item['developer'] = a.xpath('div[3]/div/a/text()').get()
        item['publisher'] = a.xpath('div[4]/div/a/text()').get()
        item['currentUsers'] = response.meta['currentUsers']
        item['dailyPeakUsers'] = response.meta['dailyPeakUsers']
        item['gameTitle'] = response.meta['gameTitle']
        item['listRank'] = response.meta['listRank']
        item['timestamp'] = datetime.datetime.utcnow()
        yield item

    def start_requests(self):
        return [scrapy.FormRequest('https://store.steampowered.com/stats/',
                        callback=self.parse)]
"""
    def parseGameData(self, response, hej):
        print(hej)
        print(response.xpath('//title/text()').get())
        item = GameMetaDataItem()



        item['developer'] = a.xpath('div[3]/div/a/text()').get() #a.xpath('div[3]/div/text()').get()
        item['publisher'] = a.xpath('div[4]/div/text()').get()

        print(a.xpath('div[3]/div/text()').get(), a.xpath('div[3]/div/a/text()').get())
        print(a.xpath('div[4]/div/text()').get(), a.xpath('div[4]/div/a/text()').get())


        yield item
"""

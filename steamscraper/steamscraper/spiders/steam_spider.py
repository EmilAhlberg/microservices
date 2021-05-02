import scrapy

class SteamSpider(scrapy.Spider):
    name = "steam"

    #start_urls = ['https://store.steampowered.com/search/?filter=topsellers']

    start_urls = ['https://store.steampowered.com/stats/']

    def parse (self, response):
        #page = response.url.split('/')[-1]


        detailStats = response.xpath('//*[@id="detailStats"]')

        currentPlayers   = detailStats.xpath('//*[@class="player_count_row"]/td[1]/span/text()')
        peakPlayers   = detailStats.xpath('//*[@class="player_count_row"]/td[2]/span/text()')
        gameTitle   = detailStats.xpath('//*[@class="player_count_row"]/td/a/text()')

        for rank, (cp, pp, gt) in enumerate(zip(currentPlayers, peakPlayers, gameTitle)):
            print(rank+1, cp.get(), pp.get(), gt.get())

        """
        topList = response.xpath('//*[@id="search_resultsRows"]')

        print(topList)


        titles = topList.xpath('//*[@class="title"]//text()')
        hrefs = topList.xpath('//a/@href')


        for t, h in zip(titles, hrefs):
            print(t.get(), ' :: ', h.get())


        print(title)


        #filename = 'steam-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(res)
        """

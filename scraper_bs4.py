import requests
from bs4 import BeautifulSoup


def fetchData(url: str) -> BeautifulSoup:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

topSellersUrl = 'https://store.steampowered.com/search/?filter=topsellers'

topSellers = fetchData(topSellersUrl).find_all('a', {'class': 'search_result_row'})

results = []

for row in topSellers:
    #print(row)
    title = row.find('span', {'class': 'title'}).text
    gameUrl = row.get('href')
    #platform = row.find('span', {'class': 'platform'}).text
    print(title)
    print(gameUrl)

    gameData = fetchData(gameUrl)
    print('...............')
    #print(gameData)

    test = gameData.find_all('div', class_='dev_row')[0:2]

    for t in test:
        print(t)
        try:
            print(t.find('div', class_='summary column').text)
            print(t.find('div', class_='subtitle column').text)
        except:
            print('error')
    #print(test)
    quit()

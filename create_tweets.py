import requests
from lxml import html


def create_tweet():
    response = requests.get('https://www.worldometers.info/coronavirus/')
    doc = html.fromstring(response.content)
    total, deaths, recovered = doc.xpath('//div[@class="maincounter-number"]/span/text()')

    tweet = f'''Coronavirus Latest Updates
    Total cases: {total}
    Recovered: {recovered}
    Deaths: {deaths}
    Source: https://www.worldometers.info/coronavirus/
    #coronavirus #covid19 #coronavirusupdates #covid19update
    '''
    return tweet


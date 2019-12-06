import requests
from bs4 import BeautifulSoup

'''def get_coments(link="google.com"):
    html = requests.get(link)
    soup = BeautifulSoup(urlopen(html), features='html.parser')
    return soup.find_all('div')


URL = 'https://play.google.com/store/apps/details?id=com.bigshotgames.legendaryItem'
link = get_coments(link=URL)
print(link)
'''


def getcomments(link):

    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('script')


comentarios = getcomments('https://play.google.com/store/apps/details?id=com.whatsapp&hl=pt&showAllReviews=true')
print(str(comentarios))
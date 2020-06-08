import requests
from bs4 import BeautifulSoup
import re

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
#    soup = soup.findAll(attrs={'nonce': re.compile(r"^5l9CeWUdLj5ADOZ1jEGf3Q$")})
    for a in soup:
        index = soup.find("key: 'ds:23'")
        if( index != -1):
            print( "achei" )
    new_String = ""
    while( index < len( soup ) ):
        new_String+= soup[index]
        index+=1
    return new_String


comentarios = getcomments('https://play.google.com/store/apps/details?id=com.whatsapp&hl=pt&showAllReviews=true')
print(str(comentarios))

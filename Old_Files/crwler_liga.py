import requests
import urllib
from bs4 import BeautifulSoup
import re
#coisas que eu quero pega do sit
class deck_informaçoes:
    nome=""
    link=""

class card_info:
    nome=""
    quantidade=""
    link=""

#funçao que vai baixa todos os decks de um jogador especifico
def baixaListaDecks(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser') 
    soup = soup.findAll(attrs={'class': re.compile(r"^dk-nome$")})
    returned = []
    for deck_name_division in soup:
        string = str(deck_name_division)
        index_start_link = len("<div class='"'dk-nome'"'><a href=")
        index_start_link+=2
        deck_link = liga_link
        index_nome_deck = index_start_link
        while(string[index_start_link] != '"'):
            deck_link+= string[index_start_link]
            index_start_link+=1
            index_nome_deck+=1
        
        index_nome_deck+=2
        nome_deck = ""
        while( string[index_nome_deck] != '<' ):
            nome_deck+=string[index_nome_deck]
            index_nome_deck+=1
        deck = deck_informaçoes()
        deck_link =deck_link.replace("amp;","")
        deck.link=deck_link
        deck.nome=nome_deck
        returned.append(deck)
    return returned

#Funçao que baixa um deck especifico
def baixaDeck( link ):
    page = requests.get(link)#cria o objeto do requeste
    soup = BeautifulSoup(page.content, 'html.parser') #faz o requeste

    HTML_to_name = soup.findAll(attrs={'class': re.compile(r"^sticky_lazy$")}) # cria variavel com filtro por classe 'sticky_lazy'
    HTML_to_quantidade = soup.findAll(attrs={'class': re.compile(r"^deck-qty$")})# cria variavel com filtro classe 'deck-qty'

    returned=[] #o que eu vo retorna
    carta = card_info()
    count1=0
    quant_total = 0
    for a in HTML_to_quantidade: # na variavel filtrada por 'deck-qty', para cado elemento ( dentro do <... class="deck-qty"> <...> )
        string = str(a) # transforma o elemento em string 
        index_qantidade = string.find("class='deck-qty'>") #procura nessa string essa outra sub string
        index_qantidade += 22 #a a posiçao que eu recebe é de quando a sub string q eu procurei comessa entao eu somo um valor pra chega onde eu quero
        quant = "" # variavel que salva algo q eu quero
        quant+= string[index_qantidade]#Inicio filtragem do que eu quero, daqui pra baixo é so filtragem pra pega o que eu quero
        index_qantidade+=1
        for i in range(0,9):
            str_i = str(i)
            if( string[index_qantidade] == str_i):
                quant+= string[index_qantidade]
        carta.quantidade=quant
        returned.append(carta)
        quant_total +=int(quant)
        if(quant_total >= 100):
            break
        count1+=1
    count2 = 0
    for a in HTML_to_name:# aqui eu to fazendo algo parecido com o loop dali de cima so que aqui eu pego o nome da carta
        string = str(a)
        index_carta = string.find("card=")
        index_carta += len("card=")
        printString = ""
        while( string[index_carta] != '"' ):
            printString += string[index_carta]
            index_carta+=1
        returned[count2].nome=printString
        print("{0} {1}".format( returned[count2].quantidade,returned[count2].nome))
        if(count2 >= count1):
            break
        count2+=1
    return returned

liga_link = "https://www.ligamagic.com.br"
link_find_dack_No_player = "https://www.ligamagic.com.br/?view=dks/decks&filtro_nome_jogador="
player = "denielfer"
link_find_dack_player = link_find_dack_No_player + player

decks = baixaListaDecks(link_find_dack_player)

for a in decks:
    deck = baixaDeck(a.link)
    input()

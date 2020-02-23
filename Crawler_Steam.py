import requests
import urllib
from bs4 import BeautifulSoup
import re


def salva_avaliaçoes(link):
    page = requests.get(link)  # cria o objeto do requeste
    soup = BeautifulSoup(page.content, 'html.parser')  # faz o requeste

    comentarios = soup.findAll(attrs={'class': re.compile(r"^review_box$")})
    salva = []
    for a in comentarios:
        salva.append(Limpa_comentario(a))
    arq = open("comentarios_bruto.txt", "a")
    arq.write("_________________________________\n")
    for c in salva:
        arq.write(c + "\n")
    arq.close


def Limpa_comentario(comentario):
    recomendação_class = str(comentario.findAll(attrs={'class': re.compile(r"^title$")}))
    comentario_class = str(comentario.findAll(attrs={'class': re.compile(r"^content$")}))
    # PEGA A PRIMEIRA LETRA do: RECOMENDAO ou NOT RECOMENDADO
    list = recomendação_class.find(">")
    list = recomendação_class.find(">", list + 1)
    recomendado = recomendação_class[list + 1]
    # Pega comentario
    comentario = comentario_class.replace('<div class="content">', '')
    comentario = comentario.replace("								</div>", "")
    return (recomendado + " : " + comentario)


def ler_lista(fileName):
    file = open(fileName.__add__('.txt'), 'r')
    lista = file.readlines()
    return lista


# alterar link para baixa de outra pessoa, em cada um dos links  é um link de analize de uma conta
filename = input("Digite o nome do arquivo que contém os links: ")
Lista_links = ler_lista(filename)
for b in Lista_links:
    salva_avaliaçoes(b)
print("Foram salvas as avaliações\nDo arquivo: "+filename)

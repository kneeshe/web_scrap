#codigo para efetuar web scraping utilizando python

from bs4 import BeautifulSoup #importa o beautifulsoup 
import requests #importa o requests. biblioteca http. usado nas requisições 
import re #importa o re. serve para fazer os testes usando regex

def validador_email(email): #faz a validação do email usando regex
    #transforma os termos em objeto. facilita a usabilidade 
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    
    if re.fullmatch(regex, email): #se o email coincidir com os termos do regex, ele é valido 
        print("email valido")
    else:
        print("email invalido")

def validador_tel(tel): #validador de numero telefonico
    expressao = ""
    regex = re.compile(expressao)

    if re.fullmatch(regex, tel):
        print("telefone valido")
    else:
        print("telefone invalido")

#def validador_cpf(cpf): #validador de cpf 

def scrap_site():
    end_site = "https://www.carrefour.com.br/busca/teclado%20yamaha%20e473" #endereço de busca 
    #cabeçalho do navegador. evita problemas com bloqueios dos sites
    cabecalho = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0"}

    requisicao = requests.get(end_site, cabecalho) #faz a tentativa de conexão com o endereço e apresenta o cabeçalho na requisição 
    print(requisicao)

    sopa = BeautifulSoup(requisicao.content,"html.parser")
    nome_tec = sopa.findAll("h2")
    preco_tec = sopa.findAll("a")

    for i in nome_tec:
        print(i['h2'])
    
    for j in preco_tec:
        print(j.text)

scrap_site()

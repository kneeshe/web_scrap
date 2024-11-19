###Codigo em python para scraping

import requests
import re
from bs4 import BeautifulSoup

##validador de cpf
def valida_cpf():
  cpf = str(input("Digite um CPF válido (com pontos e traço): "))

  #Retira apenas os dígitos do CPF, ignorando os caracteres especiais
  numeros = [int(digito) for digito in cpf if digito.isdigit()]

  formatacao = False
  quant_digitos = False
  validacao1 = False
  validacao2 = False
  
  while cpf != True:
      #Verifica a estrutura do CPF (111.222.333-44)
      if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
          formatacao = True
          return cpf  
    
      if len(numeros) == 11:
          quant_digitos = True
    
          soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
          digito_esperado = (soma_produtos * 10 % 11) % 10
          if numeros[9] == digito_esperado:
              validacao1 = True
    
          soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
          digito_esperado1 = (soma_produtos1 *10 % 11) % 10
          if numeros[10] == digito_esperado1:
              validacao2 = True
    
          if quant_digitos == True and formatacao == True and validacao1 == True and validacao2 == True:
              return cpf
          else:
              print(f"O CPF {cpf} não é válido... Tente outro CPF...")
              cpf = str(input("Digite um CPF válido (com pontos e traço): "))
    
      else:
          print(f"O CPF {cpf} não é válido... Tente outro CPF...")
          cpf = str(input("Digite um CPF válido (com pontos e traço): "))

##validador de email
def valida_email():
    padrao_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    email = input("Digite seu email: ")
    while email != True:
      if re.fullmatch(padrao_email, email):
        return email
      else:
        print("Email inválido. Por favor, tente novamente")
        email = input("Por favor, digite novamente seu email: ")


##validador de telefone
def valida_fone():
  re_fone = re.compile(r"^\s*(\d{2}|\d{0})[-. ]?(\d{5}|\d{4})[-. ]?(\d{4})[-. ]?\s*$")
  fone = input("Digite seu telefone: ")
  while fone != True:
    if re.fullmatch(re_fone, fone):
        return fone
    else:
        print("Telefone inválido. Por favor, tente novamente")
        fone = input("Por favor, digite novamente seu telefone: ")

##função de scrap
def scrap_site():

  url_site = "https://www.carrefour.com.br/busca/Teclado%20Yamaha%20PSR-E473"
  #url_pag = url_site + "ecommerce/"
  cabecalho = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"}
  proxies = {
      "http": "http://8c5906b99fbd1c0bcd0f916d545c565a6dd32b83755a2d1e75485e538813bb7d9a2ce4dde39a38f3a25269695fa58faa5c097c2615df5d00c25424f2dc3b72ae5ff1c737c538ba6671dc8837dc04fc4c:w52fbawor7mn@proxy.toolip.io:31111",
      "https": "http://8c5906b99fbd1c0bcd0f916d545c565a6dd32b83755a2d1e75485e538813bb7d9a2ce4dde39a38f3a25269695fa58faa5c097c2615df5d00c25424f2dc3b72ae5ff1c737c538ba6671dc8837dc04fc4c:w52fbawor7mn@proxy.toolip.io:31111",
  }

  conexao = requests.get(url_site, headers=cabecalho)
  print(conexao)

  soup = BeautifulSoup(conexao.text, "html.parser")
  nome_prod = soup.find_all("h2", {"class": "text-xs leading-4 text-[#333] text-left my-3 truncate-text h-12"})
  tag_preco = soup.find_all("span", {"class": "text-base font-bold text-primary"})
  link_prod = soup.find_all('a', {"class": "border rounded-lg border-[#f2f2f2] p-2 cursor-pointer overflow-hidden hover:shadow-md undefined flex flex-col gap-4"}, href=True)

  nomes = [k.text for k in nome_prod]
  valores = [i.text for i in tag_preco]
  links = [j['href'] for j in link_prod]

  dic_nome = dict(zip(nomes, valores))
  dic_links = dict(zip(valores, links))

  print(f"O nome do produto: {min(dic_nome)}\nO valor do produto: {min(dic_nome.values())}\nO link do produto: {min(dic_links.values())}")

### função principal
nome_user = input("Digite seu nome: ")

cpf_user = valida_cpf()

email_user = valida_email()

fone_user = valida_fone()


print(f"Seu nome é: {nome_user}\nSeu cpf é {cpf_user}\nSeu email é: {email_user}\nSeu telefone é: {fone_user}")

scrap_site()

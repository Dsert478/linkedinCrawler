# Vamos dar uma olhada em Agentes de usuário e web
# scraping com Python, para ver como podemos contornar
# algumas proteções básicas contra scraping. Este vídeo
# mostrará a você a aparência de uma string de agente de usuário,
# como encontrá-la e como enviá-la junto com sua solicitação,
# permitindo que você convença o servidor da web de que está vindo
# de um navegador controlado pelo usuário.

import requests
from bs4 import BeautifulSoup
"""
# Google
print('Google')
r = requests.get('http://google.com')
print(r.status_code)
print(r.request.headers)

# Instagram
print('Instagram')
headers0 = {'User-Agent': 'python-requests/2.25.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
r1 = requests.get('https://www.instagram.com/', headers0=headers0)
print(r1.status_code)
print(r1.request.headers0)

# Linkeding
print('Linkedin')
r2 = requests.get('https://www.linkedin.com/feed/')
print(r2.status_code)
print(r2.request.headers)

print('Amazon')
r3 = requests.get('https://www.amazon.co.uk/Canon-M50-Compact-System-3-5-6-3/dp/B07B19L9NK/ref=sr_1_1?dchild=1&keywords=canon+m50&qid=1593248604&sr=8-1')
#print(r3.text)
print('Status Code {}'.format(r3.status_code))
print(r3.request.headers)

# Usando o User-Agent para acessar o site Amazon
headers = {"User-Agent": "Mozilla/2.25.1 (Windows Nt 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

# è importante Acrescentar a variável header no final da requisição como mostra o exemplo abaixo
r4 = requests.get('https://www.amazon.co.uk/Canon-M50-Compact-System-3-5-6-3/dp/B07B19L9NK/ref=sr_1_1?dchild=1&keywords=canon+m50&qid=1593248604&sr=8-1', headers=headers)


"""

# Amazon
url = "https://www.amazon.co.uk/Canon-M50-Compact-System-3-5-6-3/dp/B07B19L9NK/ref=sr_1_1?dchild=1&keywords=canon+m50&qid=1593248604&sr=8-1"
headers = {"User-Agent": "Mozilla/2.25.1 (Windows Nt 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

r5 = requests.get(url, headers=headers)
soup = BeautifulSoup(r5.content, features="lxml")

price = soup.find('span', {'id': 'priceblock_ourprice'}).text
print(price)
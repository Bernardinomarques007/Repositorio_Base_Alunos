import requests, os, bs4

url = 'https://www.pygame.org/docs/'

os.makedirs('torrent_jogos', exist_ok=True)
while not url.endswith('#'):
#faz dowload da pagina
    print('dowloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

print(soup)
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from subprocess import call
from IPython.display import clear_output
from time import sleep

title = []
inti = []
situs = []

def ambil_judul(i):

    url = 'https://www.detik.com/search/searchall?query=minyak%20goreng&sortby=time&page=' + str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find(class_='list media_rows list-berita').find_all('article')
    for x in headlines:
        web_ = x.find('a').get('href')
        url1 = str(web_) +'?single=1'
        
        toi_article = Article(url1, language="id")
        #To download the article
        toi_article.download()
        #To parse the article
        toi_article.parse()
        
        #print("Sedang Parsing :", toi_article.title)
        title.append(toi_article.title)
        
        inti.append(toi_article.text)
        
        situs.append(url1)
        
    sleep(2)
        
    return title, inti, situs

        
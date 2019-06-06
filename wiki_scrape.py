import requests
from bs4 import BeautifulSoup
import lxml

def classes_scrape():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url = "https://www.dandwiki.com/wiki/5e_Classes"
    page = requests.get(url,headers=headers).text
    soup = BeautifulSoup(page,features ="lxml")
    print(soup.prettify())
classes_scrape()


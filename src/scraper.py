import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrap_web(url):
    """
    This function scrap the text from any website using url
    """
    response=requests.get(url)
    beautiful_soup=BeautifulSoup(response.content,'html.parser')
    text=beautiful_soup.get_text()
    return text
    
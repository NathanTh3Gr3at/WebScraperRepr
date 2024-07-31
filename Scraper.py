#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
    url = "http://quotes.toscrape.com"
    request=requests.get(url)
    soup=BeautifulSoup(request.content,'html.parser')
    content=soup.find('div', class_='quote')
    lines=content.find('span',class_='text')
    author=content.find('small',class_='author')
    output=f"{lines} by {author}"
    print(output)




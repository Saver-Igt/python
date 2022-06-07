import requests
from bs4 import BeautifulSoup
import re
#ссылка на видео
URL = "https://www.youtube.com/watch?v=eWa7drf-b4w"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

title = soup.find("meta", itemprop="name")["content"]
description = soup.find("meta", itemprop="description")['content']
date_published = soup.find("meta", itemprop="datePublished")['content']

print(date_published + ":" + title + " - " + description)
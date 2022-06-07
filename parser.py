import requests
from bs4 import BeautifulSoup
import re
#ссылка на канал
URL = "https://www.youtube.com/c/PseudoDeveloper"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
search = soup.find_all("script")
key = '"videoId":"'

data = re.findall(key + r"([^*]{11})", str(search))
data = list(set(data))

for i in data:
    print("https://www.youtube.com/watch?v=" + i)
    

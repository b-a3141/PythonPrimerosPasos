import requests
import urllib.request
from bs4 import BeautifulSoup as b
pagina = urllib.request.urlopen("https://openwebinars.net/")
# html = requests.get(url).text
#soup = b(pagina,features="html.parser")
soup = b(pagina)
Tag = soup("a")
for tag in Tag:
    print(tag.get("href"))

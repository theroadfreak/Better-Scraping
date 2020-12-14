from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = "https://www.neptun.mk/pocetna/categories/TV_AUDIO_VIDEO/DOMASNI_KINA/SOUNDBAR.nspx"

# opening
client = uReq(url)
pageHtml = client.read()
pageSoup = soup(pageHtml, "html.parser")
client.close()
print(pageSoup.form)

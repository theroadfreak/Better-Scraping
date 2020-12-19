from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = "https://www.neptun.mk/pocetna/categories/TV_AUDIO_VIDEO/DOMASNI_KINA/SOUNDBAR.nspx"

# opening
client = uReq(url)
pageHtml = client.read()
client.close()
pageSoup = soup(pageHtml, "html.parser")

pageSoup = pageSoup.html
pageSoup = pageSoup.body
pageSoup = pageSoup.find('form', {'id': 'aspnetForm'})
pageSoup = pageSoup.find('div', {'id': 'ns-wrapper'})
pageSoup = pageSoup.find('div', {'id': 'ns-content'})
pageSoup = pageSoup.find('div', {'class': 'full-content catPage'})
pageSoup = pageSoup.find('div', {'class': 'container'})
pageSoup = pageSoup.find('div', {'class': 'row'})
# pageSoup = pageSoup.find('div', {'class': 'inner-content-box inner'})
# pageSoup = pageSoup.div
# pageSoup = pageSoup.find('div', {'id': 'angularApp'})
# pageSoup = pageSoup.find('div', {'class': 'ng-scope'})
# pageSoup = pageSoup.find('div', {'id': 'mainContainer'})
# pageSoup = pageSoup.find('div', {'class': 'row'})
# pageSoup = pageSoup.find(
#     'div', {'class': 'col-lg-9 col-md-9 col-sm-8 col-fix-main'})

# test code


print(pageSoup)

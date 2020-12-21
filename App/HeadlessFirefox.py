from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as soup
from os import system


options = Options()
options.headless = True
driver = webdriver.Firefox(
    options=options, executable_path=r'.\\geckodriver.exe')
driver.get(
    "https://www.neptun.mk/pocetna/categories/TV_AUDIO_VIDEO/DOMASNI_KINA/SOUNDBAR.nspx")
pageSoup = soup(driver.page_source, "html.parser")
driver.quit()

pageSoup = pageSoup.findAll(
    'div', {'class': 'ng-scope product-list-item-grid'})

listOfFound = list()

for elem in pageSoup:

    title = elem.find(
        'h2', {'class': 'product-list-item__content--title ng-binding'})
    price = elem.find(
        'span', {'class': 'product-price__amount--value ng-binding'})
    img = elem.find('img', {'class': 'ng-scope'})

    listOfFound.append((title.get_text(), price.get_text(), img['src']))

template = open('indexTemplate.html', 'r')
index = open('index.html', 'w', encoding='utf-8')
template = template.read()

finalHtml = str()

for item in listOfFound:
    finalHtml += f'<h2>{item[0]}</h2> \n <h3>{item[1]}</h3> \n <img src="https://www.neptun.mk/{item[2]}"></img> \n'

index.write(template.replace('##', finalHtml))

index.close()
system('start index.html')

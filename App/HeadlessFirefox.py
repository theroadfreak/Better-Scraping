from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as soup


options = Options()
options.headless = True
driver = webdriver.Firefox(
    options=options, executable_path=r'.\\geckodriver.exe')
driver.get(
    "https://www.neptun.mk/pocetna/categories/TV_AUDIO_VIDEO/DOMASNI_KINA/SOUNDBAR.nspx")
# print(driver.page_source)
pageSoup = soup(driver.page_source, "html.parser")
driver.quit()

pageSoup = pageSoup.findAll(
    'div', {'class': 'ng-scope product-list-item-grid'})
print(len(pageSoup))
for elem in pageSoup:
    title = elem.find(
        'h2', {'class': 'product-list-item__content--title ng-binding'})
    price = elem.find(
        'span', {'class': 'product-price__amount--value ng-binding'})
    print(f"{title.get_text()} --- {price.get_text()}")
    print("-------------------------------------------------")

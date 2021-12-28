from selenium import webdriver
from bs4 import BeautifulSoup
import csv

link = "https://play.google.com/store/apps/details?id=com.telkomsel.telkomselcm&hl=id&showAllReviews=true"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(link)

title = driver.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz/c-wiz/div/div[2]/div/div[1]/c-wiz[1]/h1/span')
title_code = title.get_attribute('innerHTML')
title_html = BeautifulSoup(title_code, 'html.parser')
outputFileName = title_html.string

for x in range(50):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

reviews = driver.find_elements_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]")[0]
reviews_code = reviews.get_attribute('innerHTML')
reviews_html = BeautifulSoup(reviews_code, 'lxml')

name = reviews_html.find_all('span', attrs={"class":"X43Kjb"})
star = reviews_html.find_all('div', role='img')
tgl = reviews_html.find_all('span', attrs={"class":"p2TkOb"})
komen = reviews_html.find_all('span', attrs={"jsname":"bN97Pc"})
driver.quit()

with open(outputFileName+'.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Name","Ratings","Date","Comment"])
    for i in range(len(name)-1):
        writer.writerow([name[i].string.encode('utf-8'), star[i].get('aria-label').strip("Diberi rating ")[0], tgl[i].string, komen[i].get_text().encode('utf-8')])
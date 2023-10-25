# ________________________________________
# достает дату
# from selenium import webdriver
# from bs4 import BeautifulSoup
#
#
# driver = webdriver.Chrome()
# driver.get("https://announcements.bybit.com/en-US/article/special-offer-looking-for-a-new-crypto-card--bltaa691019e4782034/")
#
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
#
# tag = soup.find_all("span", class_='article-detail-date')
# for content in tag:
#     print(content.string)
# driver.quit()
# достает дату
# ___________________________________________________________



# ___________________________________________________
# берет адрес ссылки, но не обходит защиту ссылок
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.get("https://announcements.bybit.com/en-US/article/special-offer-looking-for-a-new-crypto-card--bltaa691019e4782034/")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

for tag in soup.find_all('div', class_='article-list'):
    print(tag)
    # href = tag['href']
    # if not href:
    #     print('нет тегов')
    # print(f"https://announcements.bybit.com{href}")

driver.quit()
# берет адрес ссылки, но не обходит защиту ссылок
# ___________________________________________________




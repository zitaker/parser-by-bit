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

from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.get("https://announcements.bybit.com/en-US/?category=&page=1")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

tag_div = soup.find_all("div", class_='article-item-date')
# tag_span = soup.find_all("div", class_='ant-typography ant-typography-ellipsis ant-typography-ellipsis-multiple-line article-item-title')

for content in tag_div:
    print(content.string)
# for content in tag_span:
#     print(content.string)
driver.quit()
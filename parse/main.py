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
# for tag in soup.find_all('div', class_='article-list'):
#     print(tag)
#     # href = tag['href']
#     # if not href:
#     #     print('нет тегов')
#     # print(f"https://announcements.bybit.com{href}")
#
# driver.quit()
# берет адрес ссылки, но не обходит защиту ссылок
# ___________________________________________________

# _______________________________________________
# модель как должно выгдлядить

# from selenium import webdriver
# import time
#
#
# url = "https://python-scripts.com/"
# driver = webdriver.Chrome()
#
# try:
#     driver.get(url=url)
#     time.sleep(3)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()

# модель как должно выгдлядить
# ________________________________________


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


url = 'https://announcements.bybit.com/en-US/?category=&page=1'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get(url=url)

    tag_a = driver.find_element(By.CLASS_NAME, 'no-style')

    tag_div = tag_a.find_element(By.CLASS_NAME, 'article-item-date')
    print(tag_div.text)

    tag_span = tag_a.find_element(By.TAG_NAME, 'span')
    print(tag_span.text)

    tag_a_href = tag_a.find_element(By.XPATH, "//a[@class='no-style']").get_attribute('href')
    print(tag_a_href)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
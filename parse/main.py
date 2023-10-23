# import selenium

# from bs4 import BeautifulSoup
# import urllib.request

from selenium import webdriver
# import time

# url = "https://announcements.bybit.com/en-US/article/special-offer-looking-for-a-new-crypto-card--bltaa691019e4782034/"
# driver = webdriver.Firefox()
# driver.get(url)
# time.sleep(5) # ждать 5 секунд пока страница загрузится
# data = driver.page_source # получить исходный код страницы
# driver.close()
#
# print(data)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# browser = webdriver.Firefox()

# driver = browser.get('https://announcements.bybit.com/en-US/article/special-offer-looking-for-a-new-crypto-card--bltaa691019e4782034/')
#                     url = "https://announcements.bybit.com/en-US/article/special-offer-looking-for-a-new-crypto-card--bltaa691019e4782034/"
#                     driver = webdriver.Firefox()
#                     driver.get(url)
#                     # assert 'Yahoo' in browser.title
#                     data = driver.page_source

    # soup = BeautifulSoup(data)
    # title = soup.p
    #
    # print(title)
# elem = browser.find_element(By.NAME, 'p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()


# h1_tag = data.find('h1')
# title_tag = data.find('title')
# description_tag = data.find('meta', attrs={'name': 'description'})
    # font_tag = data.find(style={'vertical-align': 'inherit'})

# h1 = h1_tag.text.strip() if h1_tag else ''
# title = title_tag.text.strip() if title_tag else ''
# description = description_tag['content'].strip() \
#     if description_tag else ''
    # font = font_tag.text.strip()
# <font style="vertical-align: inherit;">21 октября 2023 г.</font>
# print(font)
# return h1, title, description



# soup = BeautifulSoup(data.read(), 'html.parser').find('font', {'style': 'vertical-align: inherit;'})
# print(soup.string)

# html_content = '''<font style="vertical-align: inherit;">Some content to parse</font>'''
# rr = BeautifulSoup(html_content, 'html.parser')
# ww = rr.find('font')
# print(ww.contents[0])



driver = webdriver.Firefox()
driver.get("https://announcements.bybit.com/en-US/article/special-offer-looking-for-a-new-crypto-card--bltaa691019e4782034/")

content = driver.page_source
print(content)

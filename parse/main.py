from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def parser(urls):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get(url=urls)
        tag_a = driver.find_element(By.CLASS_NAME, 'no-style')

        tag_div = tag_a.find_element(By.CLASS_NAME, 'article-item-date')
        tag_span = tag_a.find_element(By.TAG_NAME, 'span')
        tag_a_href = tag_a.find_element(
            By.XPATH, "//a[@class='no-style']").get_attribute('href')

        return tag_div.text, tag_span.text, tag_a_href
    except Exception as ex:
        return ex
    finally:
        driver.close()
        driver.quit()


url = 'https://announcements.bybit.com/en-US/?category=&page=1'

print(parser(url))



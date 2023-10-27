from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import requests
def parser(urls):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get(url=urls)
        tag_a = driver.find_elements(By.CLASS_NAME, 'no-style')

        # tag_div = tag_a.find_element(By.CLASS_NAME, 'article-item-date')
        # tag_span = tag_a.find_element(By.TAG_NAME, 'span')
        # tag_a_href = tag_a.find_element(
        #     By.XPATH, "//a[@class='no-style']").get_attribute('href')

        # return tag_div.text, tag_span.text, tag_a_href

        all_tags = []
        for tag in tag_a:
            all_tags.append(tag)

        # return all_tags

        # with open(file_path, "w") as file:
        #     file.write(driver.page_source)

        # result = []
        # for elem in all_tags:
        #     if elem.find_element(By.CLASS_NAME, 'article-item-date'):
        #         result.append(elem.find_element(By.CLASS_NAME, 'article-item-date').text)
        # return result

        result = []
        for elem in all_tags:
            tag_div = elem.find_element(By.CLASS_NAME, 'article-item-date')
            tag_span = elem.find_element(By.TAG_NAME, 'span')
            tag_a_href = elem.find_element(
                By.XPATH, "//a[@class='no-style']").get_attribute('href')
            if tag_div and tag_span:
                result.append(f"{tag_div.text} {tag_span.text} {tag_a_href}")
                # result.append(f"{tag_a_href}")
        return result


    except Exception as ex:
        return ex
    finally:
        driver.close()
        driver.quit()


def get_items_urls(file_path):
    with open(file_path) as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    items_divs = soup.find_all("div", class_="article-item-date")

    result = []
    for elem in items_divs:
        result.append(elem.text)
    return result


url = 'https://announcements.bybit.com/en-US/?category=&page=1'
file_path = '../tests/fixtures/source-page.html'


def main():
    result = parser(url)
    print(result)
    # print(get_items_urls(file_path))


if __name__ == "__main__":
    main()

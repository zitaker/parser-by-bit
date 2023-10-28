import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from constants import URLS, DIRECTORY_PATH


def parser(urls):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get(url=urls)

        tag_a = driver.find_elements(By.XPATH, "//a[@class='no-style']")
        data = []
        for tag in tag_a:
            tag_div = tag.find_element(By.CLASS_NAME, 'article-item-date')
            tag_span = tag.find_element(By.TAG_NAME, 'span')
            data.append(
                [tag_div.text, tag_span.text, tag.get_attribute('href')])

        return data
    except Exception as ex:
        return ex
    finally:
        driver.close()
        driver.quit()


def saving_data(data):
    with open(DIRECTORY_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def main():
    data = parser(URLS)
    saving_data(data)
    print(data)


if __name__ == "__main__":
    main()

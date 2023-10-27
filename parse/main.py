from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from constants import URLS


def parser(urls):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get(url=urls)

        tag_a = driver.find_elements(By.XPATH, "//a[@class='no-style']")
        result = []
        for tag in tag_a:
            tag_div = tag.find_element(By.CLASS_NAME, 'article-item-date')
            tag_span = tag.find_element(By.TAG_NAME, 'span')
            result.append(
                f"{tag_div.text} {tag_span.text} {tag.get_attribute('href')}")
        return result
    except Exception as ex:
        return ex
    finally:
        driver.close()
        driver.quit()


def main():
    result = parser(URLS)
    print(result)


if __name__ == "__main__":
    main()

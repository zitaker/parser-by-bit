import csv
import time

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from constants import URL, NEW_DATA, TEMPORARY_DATA


def parser(url):
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) "
        "Gecko/20100101 Firefox/84.0")
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        options=options, service=Service(ChromeDriverManager().install()))

    try:
        driver.get(url=url)

        selector = driver.find_elements(
            By.XPATH, "//div[@class='article-list']/a")
        data = []
        for tag in selector:
            text = tag.find_element(By.TAG_NAME, 'span')
            link = tag.get_attribute('href')
            data.append(
                [text.text, link])

        return data
    except Exception as ex:
        return ex
    finally:
        driver.close()
        driver.quit()


def compare_lists(list_1, list_2):
    for elem_1, elem_2 in zip(list_1, list_2):
        if elem_1[1] != elem_2[1]:
            return elem_2
    return list_2


def read_temporary_data():
    with open(TEMPORARY_DATA, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    file.close()
    return data


def save_temporary_data(data):
    with open(TEMPORARY_DATA, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    file.close()


def save_new_data(data):
    time_of_appearance = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(NEW_DATA, 'a', newline='') as file:
        writer = csv.writer(file)
        data.insert(0, f"{time_of_appearance}")
        writer.writerows([data])
    file.close()


def main():
    while True:
        parsing_timeout = 1
        time.sleep(parsing_timeout)
        content = parser(URL)
        result = compare_lists(read_temporary_data(), content)

        if len(result) == 2:
            print('данных нет в файле - '
                  'сохранить данные в temporary_data и new_data')
            save_temporary_data(content)
            save_new_data(result)
        else:
            print('сохранить данные в temporary_data')
            save_temporary_data(content)

        print(main())


if __name__ == "__main__":
    main()

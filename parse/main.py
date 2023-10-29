import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from constants import URLS, NEW_DATA, TEMPORARY_DATA

from datetime import datetime
import time

        # def parser(urls):
        #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #
        #     try:
        #         driver.get(url=urls)
        #
        #         tag_a = driver.find_elements(By.XPATH, "//a[@class='no-style']")
        #         data = []
        #         for tag in tag_a:
        #             tag_div = tag.find_element(By.CLASS_NAME, 'article-item-date')
        #             tag_span = tag.find_element(By.TAG_NAME, 'span')
        #             data.append(
        #                 [tag_div.text, tag_span.text, tag.get_attribute('href')])
        #
        #         return data
        #     except Exception as ex:
        #         return ex
        #     finally:
        #         driver.close()
        #         driver.quit()
        #
        #
        # def saving_data(data):
        #     with open(NEW_DATA, 'w', newline='') as file:
        #         writer = csv.writer(file)
        #         writer.writerows(data)


def test():
    output_format = "%Y-%m-%d %H:%M:%S"
    while True:
        # получил данные и добавил текущее время
        # current_time = datetime.now().strftime(output_format)
        current_time = '1'

        # открыл данные для сравнения
        with open(TEMPORARY_DATA, 'r') as file:
            content = file.read()
            file.close()


            # сравниваю данные по ссылке или заголовку
        # for elem in content:
        if current_time not in content:
            print('сохранить данные в temporary_data')
            # СОХРАНИТЬ ВРЕМЕННЫЕ ФАЙЛЫ в temporary_data
            with open(TEMPORARY_DATA, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows('3')   # новые данные
                file.close()
                time.sleep(1)
        else:
            # если данные отличаются сохранить данные в new_data и temporary_data
            print('данных нет в файле - сохранить данные в temporary_data и new_data')
            with open(TEMPORARY_DATA, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows('2')   # новые данные
                file.close()

            # сохранить полученные данные в new_data
            with open(NEW_DATA, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows('3')  # новые данные
                file.close()
                time.sleep(1)







def main():
    # data = parser(URLS)
    # saving_data(data)
    print(test())


if __name__ == "__main__":
    main()

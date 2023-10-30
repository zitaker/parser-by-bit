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


# def parser(urls):
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
#     try:
#         driver.get(url=urls)
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#         tag_a = driver.find_elements(By.XPATH, "//a[@class='no-style']")
#         data = []
#         for tag in tag_a:
#             tag_span = tag.find_element(By.TAG_NAME, 'span')
#             data.append(
#                 [current_time, tag_span.text, tag.get_attribute('href')])
#
#         return data
#     except Exception as ex:
#         return ex
#     finally:
#         driver.close()
#         driver.quit()


def compare_list_of_lists(list_1, list_2):
    for elem_1, elem_2 in zip(list_1, list_2):
        if elem_1[1] != elem_2[1]:
            return elem_2
    return list_2


def main():
    while True:
    # получил данные и добавил текущее время
    # data = parser(URLS)

    # # открыл данные для сравнения
    # with open(TEMPORARY_DATA, 'r') as file:
    #     content = file.read()
    #     file.close()

    # полученные данные для сравнения перевел в список списков

    # сравниваю данные по ссылке или заголовку
        data = [['1', '2', '1'], ['3', '4', '1'], ['5', '4', '1'], ['5', '5', '1']]
        content = [['1', '2', '1'], ['3', '4', '1'], ['5', '4', '1'], ['5', '5', '1']]
        result = compare_list_of_lists(data, content)

        if len(result) == 3:
            # если данные отличаются сохранить данные в new_data и temporary_data
            print('данных нет в файле - сохранить данные в temporary_data и new_data')
            with open(TEMPORARY_DATA, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(content)   # новые данные
                file.close()

            # сохранить полученные данные в new_data
            with open(NEW_DATA, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows([result])  # новые данные
                file.close()
                time.sleep(1)
        else:
            print('сохранить данные в temporary_data')
            # СОХРАНИТЬ ВРЕМЕННЫЕ ФАЙЛЫ в temporary_data
            with open(TEMPORARY_DATA, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(content)  # новые данные
                file.close()
                time.sleep(1)

            print(main())







# def main(urls):
#     # data = parser(URLS)
#     # saving_data(data)
#     print(test(urls))


if __name__ == "__main__":
    main()

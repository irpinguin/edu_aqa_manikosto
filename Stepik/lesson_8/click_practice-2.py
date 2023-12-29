"""
Задание 2:

Прокликать все ссылки со статус-кодами на странице, используя алгоритм перебора элементов.
После каждого клика возвращаться на стартовую страницу.
Страница для выполнения задания: http://the-internet.herokuapp.com/status_codes
"""

import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

URL = 'https://the-internet.herokuapp.com/status_codes'
STATUS_CODES = [200, 301, 404, 500]


def init_driver() -> webdriver:
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(service=service, options=options)


def main():
    print("Start test")

    browser_instance = init_driver()
    browser_instance.get(URL)

    for item in STATUS_CODES:

        try:
            link = browser_instance.find_element('xpath', f'//a[text()="{item}"]')

            # проверяем, что ссылка ведет на страницу с нужным статус-кодом
            assert link.text == f'{item}', \
                f"The status code in the link {link.text} is different from expected {item}."

            # переходим по ссылке
            link.click()

        except NoSuchElementException:
            print(f'Link for status code {item} not found.')

        url = f'{URL}/{item}'

        try:
            # проверяем, что открыта нужная страница
            assert browser_instance.current_url == url, "The page opened is incorrect."

            # проверяем, что статус-код присутствует в тексте страницы
            opened_page_sign = browser_instance.find_element('xpath', f'//p[contains(text(), "{item} status")]')
            assert int(opened_page_sign.text.split()[4]) == item

            browser_instance.back()

        except NoSuchElementException:
            print(f"The expected status code {item} was not found on the open page {URL}/{item}.")

        print(f'\tverification of link {url} passed successfully.')

    print("End test")


if __name__ == "__main__":
    main()

import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

URL = 'https://www.freeconferencecall.com/global/pl/login'
URL_SETTINGS = 'https://www.freeconferencecall.com/profile/settings?tab=wall-editor'
FILE_TO_LOAD = 'foto.jpg'


def init_driver() -> webdriver:
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    return webdriver.Chrome(service=service, options=options)


def main():
    driver = init_driver()
    driver.get(URL)

    # авторизация
    login_fld = driver.find_element('xpath', '//input[@id="login_email"]')
    login_fld.send_keys('selenium@ya.ru')

    password_fld = driver.find_element('xpath', '//input[@id="password"]')
    password_fld.send_keys('123')

    agree_checkbox = driver.find_element('xpath', '//input[@id="gdpr_checkbox"]')
    agree_checkbox.click()

    submit_btn = driver.find_element('xpath', '//button[@id="loginformsubmit"]')
    submit_btn.click()

    # переход на страницу настроек профиля и на нужную вкладку
    driver.get(URL_SETTINGS)
    print(f'Сейчас открыта страница: {driver.current_url}')
    time.sleep(5)
    upload_fld = driver.find_element('xpath', '//input[@type="file"]')
    time.sleep(5)
    print(f'Путь для загрузки файла: {os.getcwd()}\\downloads\\foto.jpg')
    upload_fld.send_keys(f'{os.getcwd()}\\downloads\\foto.jpg')


if __name__ == "__main__":
    main()

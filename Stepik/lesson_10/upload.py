import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

URL = 'https://the-internet.herokuapp.com/upload'


def init_driver() -> webdriver:
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    return webdriver.Chrome(service=service, options=options)


def main():
    driver = init_driver()
    driver.get(URL)

    upload_fld = driver.find_element('xpath', '//input[@type="file"]')
    upload_fld.send_keys(f'{os.getcwd()}\downloads\Wasim_Akram.pdf')


if __name__ == "__main__":
    main()


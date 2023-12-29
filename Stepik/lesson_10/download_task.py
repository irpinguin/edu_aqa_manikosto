import os
from random import randint
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common import NoSuchElementException

URL = 'https://the-internet.herokuapp.com/download'


def init_driver() -> webdriver:
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    preferences = {
        "download.default_directory": f"{os.path.dirname(os.getcwd())}\\lesson_6\\downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", preferences)
    options.add_experimental_option("detach", True)

    return webdriver.Chrome(service=service, options=options)


def main():
    driver = init_driver()
    driver.get(URL)

    try:
        downloads_list = driver.find_elements('xpath', '//div[@class="example"]/a')
    except NoSuchElementException:
        print("Ссылки не найдены.")

    # print(downloads_list[0].get_attribute('href'))

    for link in downloads_list[:9]:
        if link:
            try:
                link.click()
                time.sleep(randint(1, 3))
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()
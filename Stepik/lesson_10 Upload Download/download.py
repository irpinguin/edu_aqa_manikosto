import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

URL = 'https://the-internet.herokuapp.com/download'


def init_driver() -> webdriver:
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    preferences = {
        "download.default_directory": f"{os.getcwd()}\downloads",
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

    time.sleep(1)
    driver.find_elements('xpath', '//a')[6].click()


if __name__ == "__main__":
    main()
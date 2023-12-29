import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

URL = 'https://whatismyipaddress.com/'
URL_BAD_SSL = 'https://expired.badssl.com/'


def init_driver() -> webdriver:
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--incognito")
    # options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--disable-cache")

    # options.add_argument("--no-sandbox")
    options.add_experimental_option("detach", True)

    options.page_load_strategy = 'normal'   # грузит все, 6.181369066238403 сек
    # options.page_load_strategy = 'eager'    # грузит только DOM, 0.6689958572387695

    return webdriver.Chrome(service=service, options=options)


def main():
    driver = init_driver()

    # в отличие от задания через опции, браузер сначала открывается в дефолтном размере, а потом ресайзится
    # driver.set_window_size(800, 400)

    # не рекомендуется в тестировании из-за неявного размера, например в докере в хедлесс
    # driver.maximize_window()

    start_time = time.time()

    driver.get(URL)
    # driver.get(URL_BAD_SSL)

    end_time = time.time()
    result_time = end_time - start_time
    print(result_time)

    # геолокацию выдает New York City Hall, New York, NY 10007, США
    # но ip видит истинный, конечно
    params = {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "accuracy": 100
    }
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", params)
    driver.get('https://2ip.io/ru/geoip/')


if __name__ == "__main__":
    main()

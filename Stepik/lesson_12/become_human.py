import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

# Как пройти проверку headless браузера? https://qna.habr.com/q/658889
URL1 = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'
URL2 = 'https://whatismyipaddress.com/'
TIMEOUT = 10

options = Options()
options.add_argument("--window-size=1280,1024")
options.add_argument("--disable-blink-features=AutomationControlled")     # отключение WebDriver-мода
options.add_argument("--headless")
# options.add_experimental_option("detach", True)

ua = UserAgent()
options.add_argument(f"--user-agent={ua.random}")                         # Изменение User-agent

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, TIMEOUT, poll_frequency=1)

# driver.get('https://dzen.ru')
# driver.save_screenshot('screenshot.png')


driver.get(URL2)
time.sleep(5)
driver.save_screenshot('screenshot.png')
wait.until(EC.title_is('What Is My IP Address - See Your Public Address - IPv4 & IPv6'))


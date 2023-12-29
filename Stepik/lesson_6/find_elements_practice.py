import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://hyperskill.org/tracks')
time.sleep(10)

driver.find_elements('class name', 'nav-link')[2].click()

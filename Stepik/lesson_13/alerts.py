import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

URL = 'https://demoqa.com/alerts'
TIMEOUT = 10

options = Options()
options.add_argument("--window-size=1024,800")
options.add_argument("--disable-blink-features=AutomationControlled")     # отключение WebDriver-мода
# options.add_argument("--headless")
options.add_experimental_option("detach", True)

ua = UserAgent()
options.add_argument(f"--user-agent={ua.random}")                         # Изменение User-agent

service = Service(executable_path=ChromeDriverManager(driver_version="120.0.6099.199").install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, TIMEOUT, poll_frequency=1)

driver.get(URL)

BTN_1 = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BTN_1)).click()
print("Button 1 clicked.")
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert_text = alert.text
time.sleep(3)
alert.accept()
print(f"Alert '{alert_text}' is accepted")
time.sleep(5)

BTN_3 = ("xpath", "//button[@id='confirmButton']")
wait.until(EC.element_to_be_clickable(BTN_3)).click()
print("Button 3 clicked.")
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert_text = alert.text
time.sleep(3)
alert.dismiss()
print(f"Alert '{alert_text}' is dismissed")

BTN_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BTN_4)).click()
print("Button 4 clicked.")
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert_text = alert.text
time.sleep(3)
alert.send_keys("Ввели какой-то текст")
time.sleep(3)
alert.accept()
print(f"Alert '{alert_text}' is accepted")

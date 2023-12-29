import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get('https://the-internet.herokuapp.com/dynamic_controls')

# REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
#
# driver.find_element(*REMOVE_BUTTON).click()
#
# wait.until(EC.invisibility_of_element(REMOVE_BUTTON))
#
# print('OK')

ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
TEXT_FIELD = ("xpath", "//button[@type='text']")

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
time.sleep(4)
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello")
time.sleep(4)
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "Hello"))
time.sleep(4)
print('OK')

# driver.find_element(*ENABLE_BUTTON).click()
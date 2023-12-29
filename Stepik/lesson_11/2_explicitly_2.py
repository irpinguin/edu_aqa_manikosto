from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://the-internet.herokuapp.com/dynamic_controls'
TIMEOUT = 15
REMOVE_BTN = ('xpath', '//button[text()="Remove"]')
ENABLE_BTN = ('xpath', '//button[text()="Enable"]')
TEXT_FLD = ('xpath', '//input[@type="text"]')

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, TIMEOUT, poll_frequency=1)

driver.get(URL)

# не забываем *, потому что в отличие от EC, find_element ее распаковывает аргумент
driver.find_element(*REMOVE_BTN).click()

wait.until(EC.invisibility_of_element_located(REMOVE_BTN))
print("Кнопка исчезла")

wait.until(EC.element_to_be_clickable(ENABLE_BTN)).click()
print("The Enable button was pressed.")
wait.until(EC.element_to_be_clickable(TEXT_FLD)).send_keys('test')
print("The text field prints: 'test'.")
wait.until(EC.text_to_be_present_in_element_value(TEXT_FLD, 'test'))
print("The text field contains 'test'.")

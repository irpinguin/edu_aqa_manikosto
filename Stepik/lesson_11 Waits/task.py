import time
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver'
TIMEOUT = 15
CHANGE_TEXT_BTN = ('xpath', '//button[@id="populate-text"]')
CHANGE_TEXT_TXT = ('xpath', '//h2[@class="target-text"]')
DISPLAY_BTN = ('xpath', '//button[@id="display-other-button"]')
DISPLAY_HIDDEN_BTN = ('xpath', '//button[@id="hidden"]')
ENABLE_BTN = ('xpath', '//button[@id="enable-button"]')
ENABLE_NEAR_BTN = ('xpath', '//button[@id="disable"]')
CLICK_ME_BTN = ('xpath', '//button[@class="btn btn-success"]')

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, TIMEOUT, poll_frequency=1)

driver.get(URL)


print('Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом')
print('-' * 20)
near_text = wait.until(EC.visibility_of_element_located(CHANGE_TEXT_TXT)).text
print(f'Element text nearby: {near_text}')

wait.until(EC.element_to_be_clickable(CHANGE_TEXT_BTN)).click()
print('The “Change Text to Selenium Webdriver” button was pressed.')

time.sleep(TIMEOUT)
wait.until(EC.text_to_be_present_in_element(CHANGE_TEXT_TXT, 'Selenium Webdriver'))

near_text = wait.until(EC.visibility_of_element_located(CHANGE_TEXT_TXT)).text
assert near_text == 'Selenium Webdriver', f"The text {near_text} is different from what you expected"
print(f'Element text nearby: {near_text}')


print('\nКликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”')
print('-' * 20)
wait.until(EC.element_to_be_clickable(DISPLAY_BTN)).click()
print('The “Display button after 10 seconds” button was pressed.')
time.sleep(TIMEOUT)
btn_text = wait.until(EC.visibility_of_element_located(DISPLAY_HIDDEN_BTN)).text
assert btn_text == 'Enabled', f"The button's text {btn_text} is different from what you expected"
print('The “Enabled” button was appeared.')


print('\nКликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”')
print('-' * 20)
wait.until(EC.element_to_be_clickable(ENABLE_BTN)).click()
print('The “Enable button after 10 seconds” button was pressed.')
time.sleep(TIMEOUT)
res = wait.until(EC.element_to_be_clickable(ENABLE_NEAR_BTN))
assert isinstance(res, selenium.webdriver.remote.webelement.WebElement), \
    f'Object type {type(res)} different from expected'
print('The button next to “Enabled” button is pressed.')


print('\nКликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта')
print('-' * 20)
wait.until(EC.element_to_be_clickable(CLICK_ME_BTN)).click()
print('The “Click me, to Open an alert after 5 seconds” button was pressed.')
time.sleep(TIMEOUT)
alert = wait.until(EC.alert_is_present())
assert isinstance(alert, selenium.webdriver.common.alert.Alert), \
    f'Object type {type(alert)} different from expected'

print('Alert open.')
print(f'The text is displayed in the alert:\n\t{alert.text}')
alert.accept()
print('The OK button in the alert is pressed.')

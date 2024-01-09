from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


URL = 'https://demoqa.com/dynamic-properties'
VISIBLE_AFTER_BTN = ('xpath', '//button[@id="visibleAfter"]')

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

# определение неявного ожидания
driver.implicitly_wait(10)

driver.get(URL)
driver.find_element(*VISIBLE_AFTER_BTN).click()     # распаковка кортежа

"""
Задание 1:

Заполнить все текстовые поля данными (почистить поля перед заполнением).
Проверить, что данные действительно введены, используя get_attribute() и assert.
Страница для выполнения задания: https://demoqa.com/text-box
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://demoqa.com/text-box')


full_name_fld = driver.find_element('xpath', '//input[@id="userName"]')
full_name_fld.clear()
assert full_name_fld.get_attribute('value') == ''
full_name_fld.send_keys("FirstName LastName")
assert full_name_fld.get_attribute('value') == "FirstName LastName"

full_name_fld = driver.find_element('xpath', '//input[@id="userEmail"]')
full_name_fld.clear()
assert full_name_fld.get_attribute('value') == ''
full_name_fld.send_keys("username@email.org")
assert full_name_fld.get_attribute('value') == "username@email.org"

full_name_fld = driver.find_element('xpath', '//textarea[@id="currentAddress"]')
full_name_fld.clear()
assert full_name_fld.get_attribute('value') == ''
full_name_fld.send_keys("ZIP, Country, City, Street, Building, Room")
assert full_name_fld.get_attribute('value') == "ZIP, Country, City, Street, Building, Room"

full_name_fld = driver.find_element('xpath', '//textarea[@id="permanentAddress"]')
full_name_fld.clear()
assert full_name_fld.get_attribute('value') == ''
full_name_fld.send_keys("ZIP, Country, City, Street, Building, Room")
assert full_name_fld.get_attribute('value') == "ZIP, Country, City, Street, Building, Room"

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

driver.get('https://testautomationpractice.blogspot.com/')

print(driver.find_element('class name', 'wikipedia-icon'))
print(driver.find_element('id', 'Wikipedia1_wikipedia-search-input'))
print(driver.find_element('class name', 'wikipedia-search-button'))
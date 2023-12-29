import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# driver.get('https://www.freeconferencecall.com/login')

# print(driver.find_element(By.ID, "loginformsubmit"))
# print(type(driver.find_element('id', "loginformsubmit")))
# >>> <class 'selenium.webdriver.remote.webelement.WebElement'>

driver.get('https://www.freeconferencecall.com/login?campain_tag=FCC20_WEB_ABA_0006')
time.sleep(10)
driver.find_element('id', "loginformsubmit").click()
time.sleep(10)

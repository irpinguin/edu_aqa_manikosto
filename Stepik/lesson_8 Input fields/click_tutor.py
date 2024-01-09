import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)


driver.get('https://www.freeconferencecall.com/global/pl')

login_btn = driver.find_element('xpath', '//a[@id="login-desktop"]')
login_btn.click()

email_fld = driver.find_element('xpath', '//input[@id="login_email"]')
email_fld.send_keys("anonymous")

print(email_fld.get_attribute('value'))
print(email_fld.get_attribute('maxlength'))

time.sleep(3)
email_fld.clear()
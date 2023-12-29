from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://demoqa.com/dynamic-properties'
TIMEOUT = 15
VISIBLE_AFTER_BTN = ('xpath', '//button[@id="visibleAfter"]')
ENABLE_IN_SEC_BTN = ('xpath', '//button[@id="enableAfter"]')

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, TIMEOUT, poll_frequency=1)

driver.get(URL)
button = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BTN))

# print(button)
# >>>
# <selenium.webdriver.remote.webelement.WebElement (session="10b35792bfb546069a25e5181661877d", element="2BAB8C0E38DEBE0A896EF5123AD513D2_element_15")>

# print(type(button))
# <class 'selenium.webdriver.remote.webelement.WebElement'>

print("Ready to click")
button.click()
print("The button was pressed")

button = wait.until(EC.element_to_be_clickable(ENABLE_IN_SEC_BTN))
print("Ready to click")
button.click()

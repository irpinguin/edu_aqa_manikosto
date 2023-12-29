from urllib.parse import unquote

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

URL = 'https://www.wikipedia.org/'
URL_RU = 'https://ru.wikipedia.org/'
TITLE = 'Wikipedia'
TITLE_RU = 'Википедия — свободная энциклопедия'


driver.get(URL)

curr_url = unquote(driver.current_url)
print(f'Ссылка на текущую страницу: "{curr_url}"')
assert curr_url == URL, \
    f'Адрес открытой страницы "{curr_url}" отличается от заданного "{URL}".'

curr_title = driver.title
print(f'Заголовок текущей страницы: "{curr_title}"')
assert curr_title == TITLE, \
    f'Заголовок открытой страницы "{curr_title}" отличается от заданного "{TITLE}".'

# print(driver.page_source)

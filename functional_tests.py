from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get('http:\\localhost:8000')

assert 'Django' in browser.title
# browser.quit()

print(browser.title)

sleep(10)

browser.quit()

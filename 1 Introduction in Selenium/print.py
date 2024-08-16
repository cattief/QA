from selenium import webdriver
from selenium.webdriver.common.by import By
import time
print("hello world!")
link = "google.com"
browser = webdriver.Chrome()
#browser.get(link)
browser.quit()
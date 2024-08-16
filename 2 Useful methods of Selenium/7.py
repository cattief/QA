from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/file_input.html"
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME,"firstname")
    input1.send_keys("Name")
    input2 = browser.find_element(By.NAME,"lastname")
    input2.send_keys("LastName")
    input3 = browser.find_element(By.NAME,"email")
    input3.send_keys("Name@email.com")
    addfile = browser.find_element(By.ID,"file")
    file_path = os.path.join(current_dir, 'file.txt')
    addfile.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

  

finally:
	time.sleep(5)
	browser.quit()
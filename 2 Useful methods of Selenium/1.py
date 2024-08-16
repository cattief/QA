from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "https://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID,"input_value")
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(calc(x_element.text))
    input2 = browser.find_element(By.ID,"robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.ID,"robotsRule")
    input3.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    #print(x_element.text)
    

	
finally:
	time.sleep(5)
	browser.quit()
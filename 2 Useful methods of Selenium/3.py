from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "https://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID,"num1").text
    y = browser.find_element(By.ID,"num2").text
    #print(x)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(int(x)+int(y)))
    #input1 = browser.find_element(By.ID,"answer")
    #input1.send_keys(calc(x))
    #input2 = browser.find_element(By.ID,"robotCheckbox")
    #input2.click()
    #input3 = browser.find_element(By.ID,"robotsRule")
    #input3.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    #print(x_element.text)
    

	
finally:
	time.sleep(5)
	browser.quit()
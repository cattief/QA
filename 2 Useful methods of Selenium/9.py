from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_value = browser.find_element(By.ID,"input_value").text
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(calc(x_value))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    

  

finally:
	time.sleep(5)
	browser.quit()
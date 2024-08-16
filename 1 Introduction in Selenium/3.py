from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = " http://suninjuly.github.io/find_link_text"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	value = str(math.ceil(math.pow(math.pi, math.e)*10000))
	link_new = browser.find_element(By.LINK_TEXT, value)
	link_new.click()
	input1 = browser.find_element(By.TAG_NAME, "input")
	#print("print", input1)
	input1.send_keys("Ivan")
	input2 = browser.find_element(By.NAME, "last_name")
	input2.send_keys("Petrov")
	input3 = browser.find_element(By.CLASS_NAME, "city")
	input3.send_keys("Smolensk")
	input4 = browser.find_element(By.ID, "country")
	input4.send_keys("Russia")
	button = browser.find_element(By.TAG_NAME, "button")
	button.click()
	#<button type="submit" class="btn btn-default"
	#  disabled="disabled">Submit</button>
finally:
	time.sleep(30)
	browser.quit()
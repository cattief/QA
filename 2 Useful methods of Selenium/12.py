from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    print("Done!")
    button = browser.find_element(By.ID, "book")     
    button.click()
    x_value = browser.find_element(By.ID,"input_value").text
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(calc(x_value))
    button = browser.find_element(By.ID, "solve")
    button.click()
    #message = browser.find_element(By.ID, "")

    assert "successful" in message.text
finally:
    time.sleep(12)
    browser.quit()


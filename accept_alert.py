import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
    result = math.log(abs(12*math.sin(int(x))))
    return result

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
try:
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    xElement = browser.find_element(By.ID, "input_value").text
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(xElement))
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
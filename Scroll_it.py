import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
    result = math.log(abs(12*math.sin(int(x))))
    return result

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
try:
    xElement = browser.find_element(By.ID,"input_value").text
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(calc(xElement))
    checkbox = browser.find_element(By.ID,"robotCheckbox")
    checkbox.click()
    radioButton = browser.find_element(By.ID,"robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", radioButton)
    radioButton.click()
    button = browser.find_element(By.CLASS_NAME, "btn")
    browser.execute_script("arguments[0].scrollIntoView(true);",button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
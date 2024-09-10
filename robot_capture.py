import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    result = browser.find_element(By.ID,"answer")
    result.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()
    radiobot = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobot.click()
    button = browser.find_element(By.CLASS_NAME,"btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
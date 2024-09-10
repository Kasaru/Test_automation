import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/get_attribute.html"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    image_code = browser.find_element(By.TAG_NAME, "img")
    x_element = image_code.get_attribute("valuex")
    x = x_element
    y = calc(x)
    result = browser.find_element(By.ID,"answer")
    result.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobot = browser.find_element(By.ID, 'robotsRule')
    radiobot.click()
    button = browser.find_element(By.CLASS_NAME,"btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
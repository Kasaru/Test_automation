import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait
def calc(x):
    result = math.log(abs(12*math.sin(int(x))))
    return result
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"), "100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    xElement = browser.find_element(By.ID, "input_value").text
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(xElement))
    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    time.sleep(10)
    browser.quit()

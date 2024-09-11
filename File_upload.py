import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)
try:
    firstName = browser.find_element(By.NAME, "firstname")
    firstName.send_keys("Ivan")
    lastName = browser.find_element(By.NAME, "lastname")
    lastName.send_keys("Ivanov")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("Ivan@ivanov.net")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'reg.txt')
    element = browser.find_element(By.ID,"file")
    element.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "btn")
    browser.execute_script("arguments[0].scrollIntoView(true);",button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
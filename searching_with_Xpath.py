from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.XPATH, "//input")
    for element in elements:
        element.send_keys("Fusk")

    button = browser.find_element(By.XPATH, "//div[6]/button[3]")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
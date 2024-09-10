from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    firstName.send_keys("Ivan")
    secontName = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    secontName.send_keys("Ivanov")
    eMail = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    eMail.send_keys("Ivan@bro.net")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
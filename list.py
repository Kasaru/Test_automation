from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID, "num1").text
    num_2 = browser.find_element(By.ID,"num2").text
    sum = int(num_2) + int(num_1)
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(f"{sum}")
    button = browser.find_element(By.CLASS_NAME,"btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
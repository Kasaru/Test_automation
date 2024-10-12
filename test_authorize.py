from time import sleep

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auth import login
from auth import password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def get_answer():
    answer = math.log(int(time.time()))
    return answer
def again_button_click(browser):
    try:
        browser.find_element(By.CLASS_NAME, "again-btn")
        return True
    except NoSuchElementException:
        return False

@pytest.mark.parametrize("url", ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_login(browser,url):
    link = url
    browser.get(link)
    login_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "navbar__auth"))
    )
    login_button.click()
    login_field = browser.find_element(By.NAME, "login")
    login_field.send_keys(login)
    passwd_field = browser.find_element(By.NAME, "password")
    passwd_field.send_keys(password)
    enter_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    enter_button.click()
    sleep(5)
    if again_button_click(browser):
        again_button = browser.find_element(By.CLASS_NAME, "again-btn")
        again_button.click()
    answer_area = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "textarea"))
    )
    answer_area.send_keys(get_answer())
    send_button = browser.find_element(By.CLASS_NAME,"submit-submission")
    send_button.click()
    optional_feedback = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint")))
    assert optional_feedback.text == "Correct!", f"Expected optional feedback 'Correct!', got {optional_feedback}"
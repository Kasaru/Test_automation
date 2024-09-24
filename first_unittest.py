from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_registration_1(self):
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
            input3.send_keys("IP@gmail.com")
            input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block > div.form-group.first_class > input")
            input4.send_keys("+109999129")
            input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block > div.form-group.second_class > input")
            input4.send_keys("Russia")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Welcome text should be 'Congratulations! You have successfully registered!'")

            time.sleep(3)
            browser.quit()

    def test_registration_2(self):
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
            input3.send_keys("IP@gmail.com")
            input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block > div.form-group.first_class > input")
            input4.send_keys("+109999129")
            input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block > div.form-group.second_class > input")
            input4.send_keys("Russia")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)


            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

            time.sleep(3)
            browser.quit()


if __name__ == "__main__":
    unittest.main()

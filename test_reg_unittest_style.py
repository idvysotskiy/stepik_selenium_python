import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestReg(unittest.TestCase):
    def test_reg_1(self):
        link_pass = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link_pass)

        # Заполняем обязательное поле first name
        textarea = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        textarea.send_keys('Ivan')
        # Заполняем обязательное поле last name
        textarea = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        textarea.send_keys('Ivanov')
        # Заполняем обязательное поле e-mail
        textarea = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        textarea.send_keys('Ivan@email.com')
        # Заполняем необязательное поле телефон
        textarea = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
        textarea.send_keys('+79639447845')
        # Заполняем необязательное поле Адрес
        textarea = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
        textarea.send_keys('Novosibirsk, Ivanova st. 43/70')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)

    def test_reg_2(self):
        link_pass = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link_pass)

        # Заполняем обязательное поле first name
        textarea = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        textarea.send_keys('Ivan')
        # Заполняем обязательное поле last name
        textarea = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        textarea.send_keys('Ivanov')
        # Заполняем обязательное поле e-mail
        textarea = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        textarea.send_keys('Ivan@email.com')
        # Заполняем необязательное поле телефон
        textarea = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
        textarea.send_keys('+79639447845')
        # Заполняем необязательное поле Адрес
        textarea = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
        textarea.send_keys('Novosibirsk, Ivanova st. 43/70')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()

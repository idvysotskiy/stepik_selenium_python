import pytest
from selenium.webdriver.common.by import By


class TestProductPage:
    def test_add_to_basket_btn(self, browser):
        link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
        assert button is not None, 'Button not found'
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.ui.browser import driver


class AddToCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = driver
        cls.dr.get("https://www.saucedemo.com")
        cls.dr.find_element(By.ID, "user-name").send_keys("standard_user")
        cls.dr.find_element(By.ID, "password").send_keys("secret_sauce")
        cls.dr.find_element(By.ID, "login-button").click()

    def test_add_to_cart(self):
        self.dr.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        badge = self.dr.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(badge.text, "1")
        self.dr.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        items = self.dr.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(items), 1)

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
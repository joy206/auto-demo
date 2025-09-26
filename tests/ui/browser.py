import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

_options = Options()
_options.add_argument("--headless=new") 
print("headless arg added")
_options.add_argument("--no-sandbox")
_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
            service=Service("D:\pycharm\chromedriver-win64\chromedriver-win64\chromedriver.exe"))





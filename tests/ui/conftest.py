import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session", autouse=True)
def browser():
    opt = Options()
    opt.add_argument("--headless=new")          # CI 无头
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-dev-shm-usage")
    # 本地驱动路径
    driver = webdriver.Chrome(service=Service(r"D:\pycharm\chromedriver-win64\chromedriver-win64\chromedriver.exe"))
    yield driver                                # 所有用例复用
    driver.quit()                               # 会话结束统一关
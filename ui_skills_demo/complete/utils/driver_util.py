"""
负责driver的创建与销毁
"""
import os
from pathlib import Path
from selenium import webdriver
from selenium.common import WebDriverException, SessionNotCreatedException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def get_driver(browser="chrome", headless=False):
    # 检测是否在Docker/Grid环境
    grid_url = os.getenv("SELENIUM_REMOTE_URL") or os.getenv("SELENIUM_GRID_URL")

    if grid_url:
        # Docker/Grid模式
        return _get_remote_driver(grid_url, browser, headless)
    else:
        # 本地
        return _get_local_driver(browser, headless)


def _get_remote_driver(grid_url, browser, headless):
    """Docker/Grid模式：（hub+node）"""
    options_map = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
    }

    options = options_map.get(browser.lower())

    if options is None:
        raise ValueError(f"不支持的浏览器：{browser}")

    if headless:
        options.add_argument("--headless")

    # Edge 需要特殊处理 browserName
    if browser.lower() == "edge":
        options.set_capability("browserName", "MicrosoftEdge")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )

    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)

    return driver


def _get_local_driver(browser, headless):
    """本地跑（从本地drivers目录读取浏览器驱动）"""
    drivers_path = Path(__file__).resolve().parent.parent / "drivers"

    # 根据传入的浏览器类型，从文件夹中选择对应的驱动
    driver_path = {
        "chrome": str(drivers_path / "chromedriver.exe"),
        "firefox": str(drivers_path / "geckodriver.exe")
    }

    try:
        # 谷歌浏览器
        if browser.lower() == "chrome":
            chrome_option = webdriver.ChromeOptions()

            if headless:
                chrome_option.add_argument("--headless=new")
            chrome_option.add_argument("--window-size=1920,1080")
            chrome_option.add_argument("--start-maximized")

            driver = webdriver.Chrome(
                options=chrome_option,
                service=ChromeService(driver_path["chrome"])
            )

        elif browser.lower() == "firefox":
            firefox_option = webdriver.FirefoxOptions()
            if headless:
                firefox_option.add_argument("--headless")

            driver = webdriver.Firefox(
                options=firefox_option,
                service=FirefoxService(driver_path["firefox"])
            )

        else:
            raise ValueError(f"不支持的浏览器：{browser}，仅支持chrome/firefox")

        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)

        return driver
    except (WebDriverException, SessionNotCreatedException) as e:
        raise RuntimeError(f"\n 环境异常：driver启动失败{e}") from e


def quit_driver(driver):
    if driver:
        try:
            driver.quit()
        except Exception as e:
            print(f"driver.quit() 失败: {e}")

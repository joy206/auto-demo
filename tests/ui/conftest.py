import os, platform, glob
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) # 定位到根目录

def _pick_local_driver():
    drivers_dir = os.path.join(ROOT_DIR, "drivers")
    if not os.path.isdir(drivers_dir):
        return None

    system = platform.system().lower()
    pattern = {
        "windows": "chromedriver*.exe",
        "linux": "chromedriver*",
        "darwin": "chromedriver*"
    }.get(system, "chromedriver*")

    candidates = glob.glob(os.path.join(drivers_dir, "**", pattern), recursive=True)
    # 只保留路径中匹配当前平台名的条目
    candidates = [p for p in candidates if system in os.path.normpath(p).lower()]
    if not candidates:
        return None

    driver_path = candidates[0]
    if system != "windows":
        os.chmod(driver_path, 0o755)
    return driver_path

@pytest.fixture(scope="function", autouse=True)
def browser():
    opt = Options()
    opt.add_argument("--headless=new")          # CI 无头
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-dev-shm-usage")

    driver_path = _pick_local_driver()
    if driver_path is None:
        from webdriver_manager.chrome import ChromeDriverManager
        driver_path = ChromeDriverManager().install()

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=opt)
    yield driver                                # 所有用例复用
    driver.quit()                               # 会话结束统一关
import os, platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 当前文件所在目录

@pytest.fixture(scope="function", autouse=True)
def browser():
    opt = Options()
    opt.add_argument("--headless=new")          # CI 无头
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-dev-shm-usage")

    if os.getenv("LOCAL_DRIVER") == "1":
        # 自备驱动：支持任意路径
        driver_path = os.getenv(
            "CHROME_DRIVER_PATH",
            os.path.join(
                BASE_DIR,
                "drivers",
                f"chromedriver-{platform.system().lower()}"
                f"{'.exe' if platform.system() == 'Windows' else ''}"
            )
        )
    else:
        # 自动下载驱动
        from webdriver_manager.chrome import ChromeDriverManager
        driver_path = ChromeDriverManager().install()

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=opt)
    yield driver                                # 所有用例复用
    driver.quit()                               # 会话结束统一关
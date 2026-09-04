"""
fixture：
    管理driver
    创建并返回各页面实例
"""
import json
import logging
import os
import platform
import re
import shutil
import time

from io import StringIO
from pathlib import Path
import allure
import pytest
from ui_skills_demo.complete.pages.detail_page import DetailPage
from ui_skills_demo.complete.pages.login_page import LoginPage
from ui_skills_demo.complete.pages.product_page import ProductPage
from ui_skills_demo.complete.utils import driver_util
from ui_skills_demo.complete.utils.log_util import swag_logger

formatter = logging.Formatter(
    "%(filename)s - %(levelname)s - %(message)s",
    "%Y_%m_%d %H:%M:%S"
)

BUILD_COUNTER_FILE = Path(".build_counter")


def get_next_build_order():
    # 优先从环境变量读取
    env_order = os.getenv("BUILD_NUMBER")
    if env_order:
        return int(env_order)

    # 本地：用时间戳
    return int(time.time())


@pytest.fixture
def driver():
    browser = os.getenv("BROWSER", "chrome")  # 默认 chrome，Docker 里可覆盖
    headless = os.getenv("HEADLESS", "true").lower() == "true"

    drv = driver_util.get_driver(browser, headless)
    yield drv
    driver_util.quit_driver(drv)


def pytest_runtest_setup(item):
    """每个用例开始执行前输出"""
    swag_logger.info(f"测试用例【{item.name}】开始执行")


def pytest_runtest_teardown(item):
    """每个用例执行结束后输出"""
    swag_logger.info(f"测试用例【{item.name}】执行结束")


@pytest.fixture
def login_page(driver):
    """返回登录页实例"""
    return LoginPage(driver)


@pytest.fixture
def products_page(driver, login_page):
    """登录后，返回商品页实例"""
    login_page.do_login("standard_user", "secret_sauce")
    return ProductPage(driver)


@pytest.fixture
def detail_page(driver):
    """没有前置流程，只返回商品详情页实例"""
    return DetailPage(driver)


@pytest.fixture(scope="function", autouse=True)
def failed_log_record():
    """错误用例的日志，才写入allure报告中"""
    # 每个用例执行都会新建独立的内存流
    mem_io = StringIO()
    mem_handler = logging.StreamHandler(mem_io)
    mem_handler.setFormatter(formatter)

    # 为自定义的swag_logger新增内存handler
    swag_logger.addHandler(mem_handler)

    yield mem_io

    # 用例执行完毕移除handler，避免多个用例日志串流
    swag_logger.removeHandler(mem_handler)
    mem_io.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('driver', None)
        if driver:
            screenshot = driver.get_screenshot_as_png()
            case_name = re.sub(r'[\\/:*?"<>|]', '_', item.name)

            screenshot_dir = Path(__file__).parent.parent / "failed_screenshots"
            screenshot_dir.mkdir(exist_ok=True)
            screenshot_name = f"{case_name}_failed.png"
            screenshot_file = screenshot_dir / screenshot_name

            with open(screenshot_file, "wb") as f:
                f.write(screenshot)

            # 把截图贴到报告中
            allure.attach(
                screenshot,
                f"{case_name}_failed.png",
                attachment_type=allure.attachment_type.PNG,
            )

            # 错误用例的日志贴到报告中
            log_stream = item.funcargs['failed_log_record']
            log_content = log_stream.getvalue()
            if log_content.strip():
                allure.attach(
                    log_content,
                    "当前用例专属完整日志",
                    attachment_type=allure.attachment_type.TEXT,
                )


def pytest_sessionstart(session):
    allure_dir = Path("allure-results")
    allure_dir.mkdir(exist_ok=True, parents=True)

    # 删除旧的 properties 文件（如果有）
    old_file = allure_dir / "environment.properties"
    if old_file.exists():
        old_file.unlink()

    env_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<environment>
    <parameter>
        <key>Browser</key>
        <value>Chrome</value>
    </parameter>
    <parameter>
        <key>OS</key>
        <value>{platform.system()} {platform.release()}</value>
    </parameter>
    <parameter>
        <key>Python.Version</key>
        <value>{platform.python_version()}</value>
    </parameter>
    <parameter>
        <key>Project</key>
        <value>SwagLabs UI自动化</value>
    </parameter>
</environment>
"""

    with open(allure_dir / "environment.xml", "w", encoding="utf-8") as f:
        f.write(env_xml)

    # 新增：创建 executor.json
    executor_info = {
        "name": "本地执行",  # 执行器名称
        "type": "local",  # 类型
        "buildName": "手动触发",  # 构建名称
        "buildOrder":get_next_build_order(),  # 构建序号
        "reportUrl": "",  # 报告链接
        "buildUrl": ""  # 构建链接
    }

    with open(allure_dir / "executor.json", "w", encoding="utf-8") as f:
        json.dump(executor_info, f, ensure_ascii=False, indent=2)


def pytest_sessionfinish(session, exitstatus):
    """测试结束后，自动复制 history 到 allure-results，为下次保留趋势"""
    report_history = Path("allure-report/history")
    results_dir = Path("allure-results")

    if report_history.exists():
        target = results_dir / "history"
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(report_history, target)
        print(f"历史趋势已复制到 {target}")

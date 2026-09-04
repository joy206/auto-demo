"""
登录页页面封装
"""
from ui_skills_demo.complete.locators.login_locators import LoginLocators
from ui_skills_demo.complete.pages.common_page import CommonPage
from ui_skills_demo.complete.utils.log_util import swag_logger


class LoginPage(CommonPage):

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.login_locators = LoginLocators()
        swag_logger.debug("初始化登录页LoginPage")

    def open(self):
        """打开页面"""
        swag_logger.info(f"打开登录页：{self.URL.strip()}")
        self.driver.get(self.URL)

    def input_username(self, username):
        """输入用户名"""
        self.input_text(self.login_locators.USERNAME_INPUT, username)

    def input_password(self, password):
        """输入密码"""
        self.input_text(self.login_locators.PASSWORD_INPUT, password)

    def click_login(self):
        """点击登录按钮"""
        self.click(self.login_locators.LOGIN_BTN)

    def get_error_text(self):
        """获取登录失败的错误提示信息"""
        return self.get_text(self.login_locators.ERROR_TEXT)

    def do_login(self, username, password):
        swag_logger.info(f"[登录]：用户名{username}")
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.click_login()
        swag_logger.info(f"[登录]登录完成")





"""
购买者个人信息页，页面操作封装
"""
from ui_skills_demo.complete.locators.checkinfo_locators import CheckInfoLocators
from ui_skills_demo.complete.pages.common_page import CommonPage
from ui_skills_demo.complete.pages.overview_page import OverviewPage


class CheckInfoPage(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.checkInfo_locators = CheckInfoLocators()

    def get_page_title(self):
        """获取信息页，页面标题"""
        return self.get_text(self.checkInfo_locators.INFO_PAGE_TITLE)

    def input_first_name(self, first_name):
        """输入名字"""
        self.input_text(self.checkInfo_locators.INPUT_FIRST_NAME, first_name)

    def input_last_name(self, last_name):
        """输入姓氏"""
        self.input_text(self.checkInfo_locators.INPUT_LAST_NAME, last_name)

    def input_post_code(self, post_code):
        """输入邮编"""
        self.input_text(self.checkInfo_locators.INPUT_POST_CODE, post_code)

    def click_cancel(self):
        """点击取消，返回到购物车页面"""
        self.click(self.checkInfo_locators.BTN_CANCEL)

    def click_continue(self):
        """点击继续，进入最终结算页"""
        self.click(self.checkInfo_locators.BTN_CONTINUE)

    def get_error_text(self):
        """获取输入框错误提示信息"""
        return self.get_text(self.checkInfo_locators.ERROR_TEXT)
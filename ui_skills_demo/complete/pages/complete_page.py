"""
结算完成页 页面操作封装
"""
from ui_skills_demo.complete.locators.complete_locators import CompleteLocators
from ui_skills_demo.complete.pages.common_page import CommonPage


class CompletePage(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.complete_locators = CompleteLocators()

    def back_to_home(self):
        """返回商品页"""
        self.click(self.complete_locators.BACK_HOME)

    def get_page_title(self):
        """获取结算完成页页面标题"""
        return self.get_text(self.complete_locators.COMPLETE_PAGE_TITLE)

    def get_desc(self):
        """获取页面描述"""
        return self.get_text(self.complete_locators.COMPLETE_HEADER)
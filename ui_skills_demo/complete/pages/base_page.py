"""
页面操作基类：封装各页面公共的基本操作
"""
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_skills_demo.complete.utils.log_util import swag_logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        swag_logger.debug("初始化BasePage")

    # 底层查找方法
    def find_element(self, locator, root=None):
        """等待元素存在，返回该元素"""
        swag_logger.debug(f"查找元素：{locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """查找所有匹配元素，返回列表（可能为空）"""
        swag_logger.debug(f"查找匹配的所有元素：{locator}")
        return self.driver.find_elements(*locator)

    def find_clickable(self, locator):
        """等待元素可点击，返回该元素"""
        swag_logger.debug(f"查找可点击元素：{locator}")
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible(self, locator):
        """等待元素可见，返回该元素"""
        swag_logger.debug(f"查找可见元素：{locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements_visible(self, locator):
        """等待所有匹配元素都可见，返回元素列表"""
        swag_logger.debug(f"查找所有匹配的可见元素: {locator}")
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        """点击元素"""
        swag_logger.debug(f"点击元素：{locator}")
        self.find_clickable(locator).click()

    def input_text(self, locator, text):
        """输入内容"""
        swag_logger.debug(f"输入文本：{locator} = {text}")
        el = self.find_visible(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator, root=None):
        """获取文本内容。需要处理root分支"""
        swag_logger.debug(f"获取元素{locator}的文本内容")
        # root=None 时走 find_visible 全局找；root 有值时直接 root.find_element(*locator) 内部找
        if root is None:
            element = self.find_visible(locator)
        else:
            element = root.find_element(*locator)  # 这里调的是selenium的原生
        swag_logger.debug(f"元素{locator}的文本内容为：{element.text}")
        return element.text

    def get_title(self):
        """获取窗口标题"""
        title = self.driver.title
        swag_logger.debug(f"获取页面标题：{title}")
        return title

    def get_url(self):
        """获取页面url"""
        url = self.driver.current_url
        swag_logger.debug(f"获取页面url：{url}")
        return url

    def get_dynamic_locator(self, locator, **kwargs):
        """返回动态定位元素"""
        by, value = locator
        final_value = value.format(**kwargs)
        return by,final_value

    def select_dropdown(self, locator, text):
        """下拉框选择：按可见文本选择"""
        swag_logger.debug(f"点击下拉框中的{text}")
        Select(self.find_visible(locator)).select_by_visible_text(text)
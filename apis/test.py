import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    platformVersion='10.0.0',
    automationName='uiautomator2',
    deviceName='192.168.90.101:5555',
    appPackage='com.android.settings',
    appActivity='.Settings'
)

appium_server_url = '192.168.90.101:5555'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        # desired_caps = {'platformName': 'Android',  # 平台名称
        #                 'platformVersion': '4.4.2',  # 系统版本号
        #                 'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
        #                 'appPackage': 'com.youdao.calculator',  # apk的包名
        #                 'appActivity': 'com.youdao.calculator.activities.MainActivity'  # activity 名称
        #                 }
        # self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        # self.driver.implicitly_wait(8)

        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        self.driver.implicitly_wait(8)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()

if __name__ == '__main__':
    unittest.main()
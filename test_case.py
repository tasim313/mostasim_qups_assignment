from selenium import webdriver
import allure
import pytest
from allure_commons_types import AttachmentType

@allure.severity(allure.severity.NORMAL)
class TestWhatsapp:
    def test_whatsapp(self):
        self.browser = webdriver.Chrome(
            executable_path='/home/kali/Downloads/chromedriver/chromedriver')
        self.browser.get('https://web.whatsapp.com/')
        status = self.browser.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]').is_displayed()

        if status==True:
            assert True
        else:
            assert False
        self.browser.close()

    def test_list_group(self):
        pytest.skip('Skipping test..Later I will implement..')

    def test_logout(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://web.whatsapp.com/')
        self.browser.find_element_by_id('txtUsername').send_keys('')
        self.browser.find_element_by_id('password').send_keys('')
        self.browser.find_element_by_id('btnLogin').click()
        act_title = self.browser.title
        if act_title=='WhatsApp':
            self.browser.close()
            assert True
        else:
            allure.attach(self.browser.get_screenshot_as_png(), name='TestLoginScreenshot', attachment_type=AttachmentType.PNG)
            self.browser.close()
            assert False
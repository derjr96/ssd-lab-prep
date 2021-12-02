from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings
from django.urls import reverse, resolve
from ..views import home
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from django.conf import settings


@override_settings(DEBUG=True)
@override_settings(STATICFILES_DIRS=(os.path.join(settings.BASE_DIR, 'assets'),))
class Test_Login_User_Interface(StaticLiveServerTestCase):
    """
        Selenium Login Page User Interface Test
    """

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        self.chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.url = f"{self.live_server_url}/"
        self.browser = self.chrome
        self.browser.implicitly_wait(10)
        self.browser.get(self.url)

        # find the form elements
        # self.browser.implicitly_wait(10)
        self.search = self.browser.find_element(By.ID, 'search')
        self.btnSearch = self.browser.find_element(By.ID, 'btnSearch')

        super().setUp()

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def test_successful_search(self):
        self.search.send_keys('hello')
        self.browser.implicitly_wait(10)
        self.btnSearch.click()

        assert 'Search' in self.browser.title

    # def test_login_form_invalid_email(self):
    #     """
    #         Login form with invalid email
    #
    #         'btnLogin' will be disabled and not allow user to submit the form
    #     """
    #     # populate form with data
    #     self.email.send_keys('SELECT * FROM Users WHERE user_id = 1 OR 1=1;')
    #     self.password.send_keys('johnsmithpassword')
    #
    #     enabled = self.browser.find_element(By.ID, 'btnLogin').is_enabled()
    #
    #     assert enabled is False
    #
    # def test_login_form_invalid_password_length(self):
    #     """
    #         Login form with password length < 10
    #
    #         'btnLogin' will be disabled and not allow user to submit the form
    #     """
    #     # populate form with data
    #     self.email.send_keys('johnsmith@gmail.com')
    #     self.password.send_keys('123')
    #
    #     enabled = self.browser.find_element(By.ID, 'btnLogin').is_enabled()
    #
    #     assert enabled is False
    #
    # def test_login_form_valid_form(self):
    #     """
    #         Login form with valid inputs
    #
    #         'btnLogin' will be enabled and allow user to submit the form
    #     """
    #     # populate form with data
    #     self.email.send_keys('chickennugget@gmail.com')
    #     self.password.send_keys('ChickenNugget')
    #
    #     captcha = self.browser.find_element(By.XPATH, '//*[@id="captcha2"]/div/div/iframe')
    #     captcha.click()
    #
    #     enabled = self.browser.find_element(By.ID, 'btnLogin').is_enabled()
    #
    #     assert enabled is True

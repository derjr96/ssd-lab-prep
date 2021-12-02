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

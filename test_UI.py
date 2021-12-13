from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Tests(TestCase):
    def test_search(self):
        search_request = 'проектор звездного неба'
        url = 'https://prom.ua/'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element_by_css_selector('[name="search_term"]').send_keys(search_request, Keys.ENTER)


        actualResult = browser.find_element_by_css_selector('[data-qaid="caption"]').text
        expectedResult = search_request

        assert expectedResult in actualResult
        browser.close()

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import xmlrunner


class OnboardingNegociosTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
           command_executor='http://192.168.6.250:4444/wd/hub',
           desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
        self.host_url = "http://stagging.fe.tributilabs.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_onboarding_salary_test_case(self):
        driver = self.driver
        login_url = self.host_url + "/login"
        driver.get(login_url)
        while not self.is_element_present("id", "email"):
            pass
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("lolmedo@mobeats.com.ar")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_xpath("//button[@type='submit']").click()

        wait = WebDriverWait(driver, 20)
        expected_url = self.host_url + "/dashboard"
        wait.until(lambda driver: driver.current_url == expected_url)

        driver.get("http://stagging.fe.tributilabs.com/onboarding")
        xpath_string = "//div[@id='1.1.5']/div"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        wait.until(lambda driver : not driver.find_element_by_xpath(xpath_string).text is None)

        driver.find_element_by_xpath(xpath_string).click()

        xpath_string = "//div[@id='root']/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/button"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        wait.until(lambda driver : not driver.find_element_by_xpath(xpath_string).text is None)
        driver.find_element_by_xpath(xpath_string).click()

        xpath_string = "//div[@id='1.1.5.4']/div/div/label/span"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        wait.until(lambda driver : not driver.find_element_by_xpath(xpath_string).text is None)
        self.assertTrue(u"¿Esta pensión es de fuente extranjera" in driver.find_element_by_xpath(xpath_string).text)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_element_present_by_xpath(self, xpath_string):
        try: self.driver.find_element_by_xpath(xpath_string)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)

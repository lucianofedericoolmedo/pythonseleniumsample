# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import string
import random
import xmlrunner

class TributiRegisterTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
           command_executor='http://192.168.6.250:4444/wd/hub',
           desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
        self.host_url = "http://stagging.fe.tributilabs.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def random_string(self, length):
        return ''.join(random.choice(string.ascii_letters) for m in range(length))

    def test_untitled_test_case(self):
        driver = self.driver
        register_url = self.host_url + "/register"
        driver.get(register_url)
        first_name = "usuario"
        last_name = "usuario apellido"
        while not self.is_element_present("id", "fist_name"):
            pass
        driver.find_element_by_id("fist_name").click()
        driver.find_element_by_id("fist_name").clear()
        driver.find_element_by_id("fist_name").send_keys(first_name)
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys(last_name)
        # Selecciono el rol que deseo tener
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/form/div[3]/div[2]/div/span/div/div/div").click()
        driver.find_element_by_xpath("//div[2]/div/div/div/ul/li").click()
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        random_email = "test_" + self.random_string(10) + "@tributi.com"
        driver.find_element_by_id("email").send_keys(random_email)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("confirm").clear()
        driver.find_element_by_id("confirm").send_keys("123456")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        while not self.is_element_present("id", "document_id"):
            pass
        driver.find_element_by_id("document_id").click()
        driver.find_element_by_id("document_id").clear()
        random_document_id = "test_" + str(random.randint(100000000, 999999999))
        driver.find_element_by_id("document_id").send_keys(random_document_id)
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("3334444")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        expected_url = self.host_url + "/dashboard"
        wait = WebDriverWait(driver, 20)
        wait.until(lambda driver: driver.current_url == expected_url)
        xpath_string = "//div[@id='root']/div/div/div/div[3]/a/span"
        try: self.assertEqual(first_name + " " + last_name, driver.find_element_by_xpath(xpath_string).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

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


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)

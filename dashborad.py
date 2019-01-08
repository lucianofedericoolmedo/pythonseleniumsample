# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import xmlrunner


class DashboardTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
           command_executor='http://192.168.6.250:4444/wd/hub',
           desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
        self.host_url = "http://stagging.fe.tributilabs.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_dashboard_test_case(self):
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
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div/button/span").click()
        xpath_string = "//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div/label"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        self.assertEqual("Ingresos Rentas Laborales", driver.find_element_by_xpath(xpath_string).text)
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div/button").click()
        xpath_string = "//div[@id='3.1.1']/div/label"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        wait.until(lambda driver : not driver.find_element_by_xpath(xpath_string).text is None)
        print(driver.find_element_by_xpath(xpath_string).text)
        self.assertEqual("Honorarios", driver.find_element_by_xpath(xpath_string).text)
        self.assertEqual("Servicios y comisiones", driver.find_element_by_xpath("//div[@id='3.1.2']/div/label").text)
        self.assertEqual("Salarios", driver.find_element_by_xpath("//div[@id='3.1.4']/div/label").text)
        self.assertEqual(u"Subsidios entregados por caja de compensación o similares", driver.find_element_by_xpath("//div[@id='3.1.5']/div/label").text)
        self.assertEqual(u"Retiro De Cesantías Directamente De Los Fondos", driver.find_element_by_xpath("//div[@id='3.1.6']/div/label").text)
        self.assertEqual("Retiro De Aportes Voluntarios A Pensiones Obligatorias", driver.find_element_by_xpath("//div[@id='3.1.7']/div/label").text)
        self.assertEqual("Retiro De Aportes Voluntarios A Pensiones Voluntarias En Cuentas Individuales", driver.find_element_by_xpath("//div[@id='3.1.8']/div/label").text)
        self.assertEqual("Retiro De Aportes Voluntarios A Pensiones Voluntarias En Planes Institucionales", driver.find_element_by_xpath("//div[@id='3.1.9']/div/label").text)
        self.assertEqual("Retiro De Aportes A Cuentas AFC o AVC", driver.find_element_by_xpath("//div[@id='3.1.0010']/div/label").text)
        self.assertEqual("Ingresos Renta de Pensiones", driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div/div/div/label").text)
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div/div/div/button").click()
        text_pensiones_de_jubilacion = 'Ingresos Por Pensiones De Jubilaci'
        print(driver.find_element_by_xpath("//div[@id='3.2.1']/div/label").text)
        xpath_string = "//div[@id='3.2.1']/div/label"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        wait.until(lambda driver : not driver.find_element_by_xpath(xpath_string).text is None)
        self.assertTrue(u'Ingresos Por Pensiones De Jubilaci' in driver.find_element_by_xpath(xpath_string).text, "No se encontro " + text_pensiones_de_jubilacion)
        self.assertEqual("Ingresos Renta de Pensiones Ingreso Rentas de Capital", driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[3]/div/div/div/div/label").text)
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[3]/div/div/div/div/button").click()
        xpath_string = "//div[@id='3.3.1']/div/label"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        wait.until(lambda driver : not driver.find_element_by_xpath(xpath_string).text is None)
        self.assertEqual("Ingresos Por Intereses en Productos Bancarios", driver.find_element_by_xpath(xpath_string).text)
        self.assertEqual(u"Ingresos Por Intereses en Fondos de Inversión, Valores o Mutuos", driver.find_element_by_xpath("//div[@id='3.3.2']/div/label").text)
        self.assertEqual("Ingresos Por Intereses Por Prestamos a Terceros", driver.find_element_by_xpath("//div[@id='3.3.3']/div/label").text)
        self.assertEqual("Ingresos Por Intereses Presuntivos", driver.find_element_by_xpath("//div[@id='3.3.4']/div/label").text)
        self.assertEqual("Arrendamientos y Alquileres", driver.find_element_by_xpath("//div[@id='3.3.5']/div/label").text)
        self.assertEqual(u"Regalías, propiedad intelectual o derechos de autor", driver.find_element_by_xpath("//div[@id='3.3.6']/div/label").text)
        self.assertEqual("Rentas por Dividendos y Participaciones", driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[4]/div/div/div/div/label").text)
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[4]/div/div/div/div/button").click()
        xpath_string = "//div[@id='3.4.1']/div/label"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        wait.until(lambda driver : not driver.find_element_by_xpath(xpath_string).text is None)
        #self.assertEqual("Ingresos Por Dividendos", driver.find_element_by_xpath(xpath_string).text)
        self.assertEqual("Rentas no Laborales", driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[5]/div/div/div/div/label").text)
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[5]/div/div/div/div/button").click()
        xpath_string = "//div[@id='3.5.1']/div/label"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        wait.until(lambda driver : not driver.find_element_by_xpath(xpath_string).text is None)
        self.assertEqual("Venta De Acciones o Participaciones En Sociedades", driver.find_element_by_xpath(xpath_string).text)
        self.assertEqual(u"Vendí Otro Bien Raíz (Incluye Lotes)", driver.find_element_by_xpath("//div[@id='3.5.3']/div/label").text)
        self.assertEqual(u"Vendí Mi Casa", driver.find_element_by_xpath("//div[@id='3.5.2']/div/label").text)
        self.assertEqual(u"Vendí Mi Vehículo U Otro Artículo Personal", driver.find_element_by_xpath("//div[@id='3.5.4']/div/label").text)
        self.assertEqual(u"Vendí Patentes, Propiedad Industrial, Literaría, Artística y Científica, Marca o Derechos de Autor", driver.find_element_by_xpath("//div[@id='3.5.5']/div/label").text)
        self.assertEqual(u"Liquidación Sociedad Conyugal", driver.find_element_by_xpath("//div[@id='3.5.0014']/div/label").text)
        self.assertEqual("Ingresos Por Seguros De Vida", driver.find_element_by_xpath("//div[@id='3.5.6']/div/label").text)
        self.assertEqual(u"Ingresos Por Seguros De Daño Emergente", driver.find_element_by_xpath("//div[@id='3.5.7']/div/label").text)
        self.assertEqual("Ingresos Por Seguros De Lucro Cesante", driver.find_element_by_xpath("//div[@id='3.5.8']/div/label").text)
        self.assertEqual("Ingresos Por Indemnizaciones (Judiciales, demandas contra el estado)", driver.find_element_by_xpath("//div[@id='3.5.9']/div/label").text)
        self.assertEqual(u"Ingresos Por Apoyo Ecónomico Para Programas Educativos", driver.find_element_by_xpath("//div[@id='3.5.0010']/div/label").text)
        self.assertEqual(u"Ingresos Por Donaciones Para Partidos Políticos", driver.find_element_by_xpath("//div[@id='3.5.0011']/div/label").text)
        self.assertEqual(u"Ingresos Por Indemnización O Compensación Por Destrucción o Renovación de Cultivos", driver.find_element_by_xpath("//div[@id='3.5.0012']/div/label").text)
        self.assertEqual(u"Ingresos Por Subsidio Para La Producción Agricola", driver.find_element_by_xpath("//div[@id='3.5.0013']/div/label").text)
        self.assertEqual("Ingresos por un Negocio", driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[6]/div/div/div/div/label").text)
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[6]/div/div/div/div/button/i").click()
        xpath_string = "//div[@id='3.6.1']/div/label"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        wait.until(lambda driver : not driver.find_element_by_xpath(xpath_string).text is None)
        #self.assertEqual("Negocio", driver.find_element_by_xpath(xpath_string).text)
        self.assertEqual("Ingresos Ocasionales", driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[7]/div/div/div/div/label").text)
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[7]/div/div/div/div/button").click()
        xpath_string = "//div[@id='3.7.1']/div/label"
        while not self.is_element_present_by_xpath(xpath_string):
            pass
        wait.until(lambda driver : not driver.find_element_by_xpath(xpath_string).text is None)
        self.assertTrue(u"Premios y Loterías" in driver.find_element_by_xpath(xpath_string).text)
        self.assertEqual("Recompensa", driver.find_element_by_xpath("//div[@id='3.7.2']/div/label").text)
        self.assertEqual(u"Herencia, Legado o Donación", driver.find_element_by_xpath("//div[@id='3.7.3']/div").text)

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

import time

import allure
from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver

@allure.title('Регистрация')
@allure.severity(Severity.MINOR)
def test_register():
    driver = WebDriver(executable_path='D://Program Files//chromedriver_win32//chromedriver.exe')
    driver.get('http://demowebshop.tricentis.com/')
    with allure.step('переход на регистрацию'):
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').click()
        driver.find_element_by_id('FirstName').send_keys('dfxfgh')
        driver.find_element_by_id('LastName').send_keys('dfxfgh')
        driver.find_element_by_id('Email').send_keys('dfghn5h@gfgmv.ff')
        driver.find_element_by_id('Password').send_keys('dfxfgh')
        driver.find_element_by_id('ConfirmPassword').send_keys('dfxfgh')
    with allure.step('Регистрация'):
        driver.find_element_by_name('register-button').click()
        time.sleep(2)
    with allure.step('Подтвержение успешной регистрации'):
        reg = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]')
        assert "Your registration completed" == reg.text

@allure.title('Тест добавления в корзину')
@allure.severity(Severity.BLOCKER)
def test_addToCart():
    driver = WebDriver(executable_path='D://Program Files//chromedriver_win32//chromedriver.exe')
    driver.get('http://demowebshop.tricentis.com/')
    with allure.step('Поиск элемента'):
        elem = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[3]/div/div[2]/h2/a')
        name = driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[3]/div/div[2]/h2/a').get_attribute("value")
        elem.click()
    with allure.step('Добавление в корзину'):
        time.sleep(2)
        item_name = driver.find_element_by_xpath(
            '//*[@id="product-details-form"]/div/div[1]/div[2]/div[1]/h1').get_attribute("value")
        assert name == item_name
        driver.find_element_by_css_selector('.add-to-cart-button').click()


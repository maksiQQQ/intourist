from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class SeleniumTest(TestCase):
    def test_one(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text('Создать место').click()
        name = driver.find_element_by_name('name')
        name.send_keys('Тестовое имя')

        location = driver.find_element_by_name('location')
        location.send_keys('Тестовая запись')

        description = driver.find_element_by_name('description')
        description.send_keys('Тестовое описание')

        button = driver.find_element_by_xpath("//*[contains(text(), 'Сохранить')]")
        button.click()
        sleep(5)

        # elem.clear()
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        driver.close()


class ProfileTestCase(TestCase):
    def test_open_profile_edit(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/profile")

        element = driver.find_element_by_xpath("//*[contains(text(), 'Редактировать')]")
        element.click()
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login


#стандартного юзера и правильный пароль передаются в фаргументах функции login

def test_successful_login(driver):
    login(driver)

    assert "inventory" in driver.current_url


#неправильный вароль передаю через тоже через аргументы функции login

def test_login_with_wrong_password(driver):
    login(driver, password="wrong_password")

    error_message = driver.find_element(
        By.CSS_SELECTOR,
        '[data-test="error"]'
    )

    assert "Username and password do not match" in error_message.text


def test_empty_login(driver):
    login(driver, user_name="")

    error_message = driver.find_element(
        By.CSS_SELECTOR,
        '[data-test="error"]'
    )

    assert "Epic sadface: Username is required" in error_message.text


def test_empty_password(driver):
    login(driver, password="")

    error_message = driver.find_element(
        By.CSS_SELECTOR,
        '[data-test="error"]'
    )

    assert "Epic sadface: Password is required" in error_message.text



def test_close_error_button(driver):
    login(driver, password="")

    driver.find_element(
        By.CSS_SELECTOR,
        '[data-test="error"] .svg-inline--fa.fa-xmark'
    ).click()

        #find_elements(), потому что он возвращает пустой список, если элемент отсутствует
    error_window = driver.find_elements(
        By.CSS_SELECTOR,
        '[data-test="error"]'
    )

    assert not error_window

def test_waiting_authorisation(driver):
    login(driver, user_name="performance_glitch_user")

    element = WebDriverWait(driver, 10).until(    #добавила ожидаение
        EC.visibility_of_element_located(  #жду пока лого станицы каталога не отобразится
            (By.CSS_SELECTOR, ".app_logo") #исли искать по классам в css селекторах - не завывать использовать вначале точку
        )
    )

    assert element.text == "Swag Labs"
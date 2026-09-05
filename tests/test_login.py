import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helpers import login


#стандартного юзера и правильный пароль передаются в фаргументах функции login

def test_successful_login(driver):
    login(driver, "standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


#неправильный вароль передаю через тоже через аргументы функции login

def test_login_with_wrong_password(driver):
    login(driver, "secret_sauce", "wrong_password")

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

    error_window = driver.find_elements(
        By.CSS_SELECTOR,
        '[data-test="error"]'
    )

    assert not error_window

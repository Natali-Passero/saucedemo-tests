import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#авторизация - теперь это функция, которая принимает параметры барузер, юзернейм и пароль
def login(driver, user_name, password):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(user_name)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    
    return driver

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




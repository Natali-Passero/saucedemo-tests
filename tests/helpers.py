import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL_STAND = "https://www.saucedemo.com/"

#авторизация - теперь это функция, которая принимает параметры барузер, юзернейм и пароль
def login(driver, user_name = "standard_user", password = "secret_sauce", tap=True):
    driver.get(URL_STAND)

    driver.find_element(By.ID, "user-name").send_keys(user_name)
    driver.find_element(By.ID, "password").send_keys(password)

    login_button = driver.find_element(By.ID, "login-button") 
    if tap:
        login_button.click()

    return driver
    
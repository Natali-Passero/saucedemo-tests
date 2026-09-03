import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()

    yield browser

    browser.quit()
    

# @pytest.fixture()
# def good_login_user(driver):
#     driver.get("https://www.saucedemo.com/")
    
#         ##assert "saucedemo" in driver.title
    
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()

#     return driver #возвращаем driver, так как без этого будет None


# @pytest.fixture()
# def bad_login_user(driver):
#     driver.get("https://www.saucedemo.com/")

#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("wrong_password")
#     driver.find_element(By.ID, "login-button").click()

#     return driver  #то же. возвращаем driver, так как без этого будет None


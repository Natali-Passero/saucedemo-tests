# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# from tests.conftest import driver


# @pytest.mark.parametrize(
#     "username, password, expected_text",
#     [
#         ("standard_user", "secret_sauce", "Products"),
#         ("standard_user", "wrong_password", "Epic sadface"),
#     ],
# )
# def test_login_mass(username, password, expected_text):
#     driver = webdriver.Chrome()
#     driver.get("https://www.saucedemo.com/")

#     driver.find_element(By.ID, "user-name").send_keys(username)
#     driver.find_element(By.ID, "password").send_keys(password)
#     driver.find_element(By.ID, "login-button").click()

#     assert expected_text in driver.page_source
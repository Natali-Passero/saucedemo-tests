from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#перенесла "хорошие" данные для входа в фикстуру, в conftest

def test_successful_login(good_login_user):
    assert "inventory" in good_login_user.current_url


#перенесла "плохие" данные для входа в фикстуру, в conftest
def test_login_with_wrong_password(bad_login_user):

    error_message = bad_login_user.find_element(
        By.CSS_SELECTOR,
        '[data-test="error"]'
    )

    assert "Username and password do not match" in error_message.text




import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helpers import login


def test_add_product_to_cart(driver):
    login(driver, "standard_user", "secret_sauce")
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack" #нажать кнопку добавления рюкзака в корзину
    ).click()

    cart_badge = driver.find_element(
        By.CSS_SELECTOR,
        ".shopping_cart_badge" #найти индикатор корзины
    )

    assert cart_badge.text == "1" #проверить, что количество товаров равно 1

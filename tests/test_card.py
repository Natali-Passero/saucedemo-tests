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



#тест нужно оптимизировать, не самый лучший assert
def test_remove_product_from_cart(driver):
    login(driver)
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack" #добавляю в корзину товар
    ).click()
    driver.find_element(
        By.ID,
        "remove-sauce-labs-backpack"  #нахожу кнопку ремув
    ).click()

    remove_from_cart = driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"  
        )

    assert remove_from_cart.text == "Add to cart" #жду что вернется в исходное состояние









    id="remove-sauce-labs-backpack"
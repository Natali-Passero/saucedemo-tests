# Учуь автоматизации на SauceDemo :)

Учебный проект по автоматизации UI-тестирования сайта SauceDemo.

## Технологии

- Python
- Selenium
- pytest
- webdriver-manager
- Git
- GitHub

## Автоматизированные тесты

Проект содержит следующие тестовые сценарии:

1. Успешная авторизация.
2. Авторизация с неверным паролем.
3. Добавление рюкзака в корзину.

## Установка проекта

0. Клонировать репозиторий:
```bash
git clone https://github.com/ТВОЙ_USERNAME/saucedemo-tests.git
```
1. Перейти в папку проекта
```bash 
cd saucedemo-tests
```
2. Создать виртуальное окружение 
```bash 
python -m venv .venv
```
3. Активировать виртуальное окружение 
```bash 
.venv\Scripts\Activate.ps1
```
4. Установить зависимости 
```bash 
python -m pip install -r requirements.txt
```
5. Запуск тестов 
```bash 
python -m pytest -v
```

###Данные для успешной авторизации:
Username: standard_user
Password: secret_sauce

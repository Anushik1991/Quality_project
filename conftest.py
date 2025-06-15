from selenium import webdriver
import pytest
import logging
import os
from datetime import datetime
import allure

# yield — это ключевой механизм фикстур в pytest, который позволяет разделить подготовку и завершение (teardown).
# yield в pytest.fixture():
# передаёт объект в тест
# позволяет указать "что делать после теста" (teardown)
# используется для управления ресурсами: браузеры, БД, файлы и т.п.


@pytest.fixture()
def get_driver():
    driver = webdriver.Chrome() # Подготовка: создаём ресурс
    driver.maximize_window()
    yield driver   # Передаём объект в тест
    driver.quit()  # Teardown: закрываем браузер


@pytest.fixture()
def get_logger(request):
    today_date = datetime.today().date()
    os.makedirs(f"logs_{today_date}", exist_ok=True)
    test_name = request.node.name
    log_path = os.path.join(f"logs_{today_date}", test_name)

    # Configure logger
    logger = logging.getLogger(test_name)
    file_handler = logging.FileHandler(log_path, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    logger.info(f'{test_name} is started')
    yield logger  # Pause the fixture  and pass logger to test
    logger.info(f'{test_name} is finished')

#Allure add the screenshot in report allure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call":
        if result.outcome == 'failed':
            allure.attach(
                item.funcargs.get("test_driver").get_screenshot_as_png(),
                name=f"{item.name}_screen",
                attachment_type=allure.attachment_type.PNG)


'''
@pytest.fixture(params=["chrome", "firefox", "edge"])
def get_driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService())
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()
    '''

# Файл conftest.py — это специальный конфигурационный файл для Pytest, 
# в котором ты можешь хранить общие настройки и логику, используемые во многих тестах.

# Основное назначение conftest.py

# * Создание общих фикстур
# * Настройка тестового окружения
# * Переопределение Pytest-хуков
# * Подключение плагинов и расширений
# * Управление глобальными ресурсами (драйвер, база данных и т.д.)

#  Область видимости
# conftest.py работает автоматически — импортировать его не нужно
# conftest.py  ← глобальный для всех тестов
# Все тесты в текущей папке и во вложенных подпапках видят фикстуры и настройки из conftest.py
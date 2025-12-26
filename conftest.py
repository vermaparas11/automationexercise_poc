import pytest
import allure
from utils.driver_factory import get_driver

@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome =yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name ="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
import pytest
import allure
import os
from utils.driver_factory import get_driver


# ---------------- Driver Fixture ----------------
@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# ---------------- Pytest Hook: Logs + Screenshot ----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # -------- Attach execution logs for every test --------
    if report.when == "call":
        log_dir = "logs"
        if os.path.exists(log_dir):
            log_files = os.listdir(log_dir)
            if log_files:
                latest_log = max(
                    [os.path.join(log_dir, f) for f in log_files],
                    key=os.path.getctime
                )

                if os.path.getsize(latest_log) > 0:
                    with open(latest_log, "r", encoding="utf-8") as f:
                        allure.attach(
                            f.read(),
                            name="Execution Logs",
                            attachment_type=allure.attachment_type.TEXT
                        )

    # -------- Attach screenshot only on failure --------
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )


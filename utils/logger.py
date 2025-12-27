import logging
import os
from datetime import datetime
import allure


# ---------- Log directory ----------
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# ---------- One log file per test run ----------
LOG_FILE = os.path.join(
    LOG_DIR,
    f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)


# ---------- Custom Allure Log Handler ----------
class AllureLogHandler(logging.Handler):
    """
    Sends logs directly to Allure during test execution.
    This guarantees logs appear in Allure report.
    """

    def emit(self, record):
        try:
            log_entry = self.format(record)
            allure.attach(
                log_entry,
                name="Execution Log",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception:
            # Never fail test because of logging
            pass


# ---------- Logger Factory ----------
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False   # Prevent duplicate logs

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        # ---------- File handler ----------
        file_handler = logging.FileHandler(
            LOG_FILE, mode="a", encoding="utf-8"
        )
        file_handler.setFormatter(formatter)

        # ---------- Console handler ----------
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # ---------- Allure handler ----------
        allure_handler = AllureLogHandler()
        allure_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        logger.addHandler(allure_handler)

    return logger

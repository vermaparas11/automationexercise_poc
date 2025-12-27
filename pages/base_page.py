from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.logger = get_logger(self.__class__.__name__)

    def scroll_into_view(self, locator):
        self.logger.info(f"Scrolling element into view: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )
        self.logger.info("Element scrolled into view successfully")
        return element

    def click(self, locator):
        self.logger.info(f"Clicking on element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
            self.logger.info("Element clicked successfully")
        except Exception as e:
            self.logger.warning(
                f"Normal click failed due to [{type(e).__name__}]. "
                f"Falling back to JavaScript click."
            )
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info("Element clicked using JavaScript")

    def get_text(self, locator):
        self.logger.info(f"Fetching text from element: {locator}")
        text = self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text
        self.logger.info(f"Text retrieved: '{text}'")
        return text

    def hover(self, locator):
        self.logger.info(f"Hovering over element: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
        self.logger.info("Hover action performed successfully")

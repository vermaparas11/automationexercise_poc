from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def scroll_into_view(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except Exception:
            # Fallback for intercepted clicks
            self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def hover(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
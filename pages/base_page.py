from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import os


class BasePage:
    """
    Base Page Object - Parent class for all page objects
    
    Why we use this:
    - Avoids code duplication (write once, use everywhere)
    - Provides common methods all pages need
    - Makes tests more maintainable
    - Uses explicit waits (best pactice for Selenium)
    
    """

    def __init__(self, driver):
        """Initialize base page with WebDriver"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) # 10 second timeout

    def find_element(self, locator):
        """
        Find single element with explicit wait

        Args:
            locator: Tuple of (By.TYPE, "locator_value")

        Returns:
            WebElement: Found element

        Why explicit wait? More reliable than implicit wait or sleep
        """
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Element not found: {locator}")
            self.take_screenshot(f"element_not_found_{locator[1]}")
            raise

    def click(self, locator):
        """
        Click element with wait for it to be clickable

        Why wait for clickable: Element might be present but not clickable yet
        """
        element = self.wait.until(EC.element_to_be_lickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """
        Clear field and enter text

        Why we clear first? Avoid appending to existing text
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from element"""
        return self.find_element(locator).text
    
    def is_displayed(self, locator):
        """
        Check if element is displayed
        
        Returns True if displayed, False if not or if element not found
        """
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False
        
    def get_current_url(self):
        """Get current page URL"""
        return self.driver.current_url
    
    def take_screenshot(self, name):
        """
        Take screenshot for debugging

        Saves to screenshots folder with timestamp
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"

        # Creabte screenshots directory if it doesn't exist
        os.makedirs("screenshots", exist_ok=True)

        self.driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")
        return filename
    
       


            

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Login Page Object for Sauce Demo

    URL: https://www.saucedemo.com/

    This page handles all login interactions:
    -Enter username
    -Enter password
    -Click login button
    - Verify error messages
    """
    # Page URL
    URL = "https://www.saucedemo.com/"

    # Locators - All login page elements
    # Why use tuples: Selenium expects (By.TYPE, "value") format
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error-button']")
    ERROR_BUTTON = (By.CSS_SELECTOR, ".error-button")

    def __init__(self, driver):
        """Initialize login page"""
        super().__init__(driver)  # Call parent constructor

    def open(self):
        """
        Navigate to login page

        Returns self for method chaining
        """
        self.driver.get(self.URL)
        return self
    
    def enter_username(self, username):
        """
        Enter username into username field

        Args:
            username: String username to enter
        """
        self.enter_text(self.USERNAME_FIELD, username)
        return self
    
    def enter_password(self, password):
        """
        Enter password into password field

        Args:
            password: String password to enter
        """
        self.enter_text(self.PASSWORD_FIELD, password)
        return self
    
    def click_login_button(self):
        """Click the login button"""
        self.click(self.LOGIN_BUTTON)
        return self
    
    def get_error_message(self):
        """
        Get error message text

        Returns:
            str: Error message text or empty string if not displayed
        """
        if self.is_displayed(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
    
    def is_error_displayed(self):
        """
        Check if error message is displayed

        Returns:
            bool: True if error message is displayed, False otherwise
        """
        return self.is_displayed(self.ERROR_MESSAGE)
    
    def login(self, username, password):
        """
        Complete login flow

        Convenience method that does entire login in one call

        Args:
            username (str): Username
            password (str): Password
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self


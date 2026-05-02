from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):
    """
    Products Page Object for Sauce Demo
    
    This page appears after successful login.
    Shows list of products user can purchase.
    
    URL: https://www.saucedemo.com/inventory.html
    """
    
    # Expected URL after login
    URL = "https://www.saucedemo.com/inventory.html"

    # Locators for products page elements
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        """Initialize products page"""
        super().__init__(driver)

    def get_title(self):
        """
        Get page title text
        
        Returns:
            str: Title text (should be "Products")
        """
        return self.get_text(self.PAGE_TITLE)
    
    def is_on_products_page(self):
        """
        Verify we're on products page
        
        Checks:
        - URL contains "inventory"
        - Inventory container is displayed
        
        Returns:
           bool: True is on products page
        """
        url_correct = "inventory" in self.get_current_url()
        container_displayed = self.is_displayed(self.INVENTORY_CONTAINER)
        return url_correct and container_displayed
    
    def get_product_count(self):
        """
        Get number of products displayed on page
        
        Returns:
            int: Number of products
        """
        products = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(products)
    
    def is_products_page_loaded(self):
        """
        Check if products page is fully loaded
    
        Returns:
            bool: True if page is loaded successfully, False otherwise
        """
        return self.is_displayed(self.PAGE_TITLE) and \
               self.get_title() == "Products"
    
    
import selenium
import pytest
import time
from selectionsPaths import Homepage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def driver():
    """Fixture to initialize and quit WebDriver."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://hrango.com/")
    yield driver # Provide driver & wait instance to test functions
    driver.quit()


class TestHRango:
    """Test Suite for HRango Website"""

    def test_homepage_loading(self, driver):
        """Test if HRango page loads"""

        try:
            assert "AI Integrated HRM Software & Solutions - HRango" in driver.title, "Page not found"
            print("Page loaded successfully")

        except AssertionError  as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_homepage_ui(self, driver):
        """Test if HRango homepage logo is displayed"""

        try:
            logo = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, Homepage.webLogo)))
            assert logo.is_displayed(), "The logo was not displayed"
            print("Logo is displayed")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")


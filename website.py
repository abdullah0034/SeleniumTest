from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selectionsPaths
from selectionsPaths import HomePageTopNav, LoginPage, signupform
from selenium.common.exceptions import NoAlertPresentException, ElementNotInteractableException, NoSuchElementException
import time
import pytest



@pytest.fixture(scope="class")
def driver():
    """Setup WebDriver instance for the test class"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


# Test suite for home page

@pytest.mark.usefixtures("driver")
class TestHrangoHomePage:

    def test_homepage_loads(self, driver):
        """Test if the homepage loads correctly"""
        try:
            driver.get("https://hrango.com/")
            assert "AI Integrated HRM Software & Solutions - HRango" in driver.title, "HRANGO homepage did not load correctly"
            print("Homepage loaded successfully")
        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_logo_display(self, driver):
        """Test if the logo is displayed"""
        try:
            logo = driver.find_element(By.XPATH, selectionsPaths.HomePageTopNav.HRango)
            assert logo.is_displayed(), "Logo not found"
            print("Logo found successfully")
        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_login_button_display(self, driver):
        """Test if the login button is displayed"""
        try:
            login_button = driver.find_element(By.XPATH, selectionsPaths.HomePageTopNav.loginBtn)
            assert login_button.is_displayed(), "Login button not found"
            print("Login button found successfully")
        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_navigation_buttons(self, driver):

        wait = WebDriverWait(driver, 20)

        """Test if all the navigation buttons are displayed"""
        try:
            home_button = wait.until(EC.visibility_of_element_located((By.XPATH, selectionsPaths.HomePageTopNav.homeBtn)))
            assert home_button.is_displayed(), "Home button is not displayed"
            print("Home navigation button is displayed")

            pricing_button = wait.until(EC.visibility_of_element_located((By.XPATH, selectionsPaths.HomePageTopNav.pricingBtn)))
            assert pricing_button.is_displayed(), "Pricing button is not displayed"
            print("Pricing navigation button is displayed")

            contact_button = wait.until(EC.visibility_of_element_located((By.XPATH, selectionsPaths.HomePageTopNav.contactBtn)))
            assert contact_button.is_displayed(), "Contact button not found"
            print("Contact button displayed")

            features_button = wait.until(EC.visibility_of_element_located((By.XPATH, selectionsPaths.HomePageTopNav.featuresBtn)))
            assert features_button.is_displayed(), "Features button not found"
            print("Features button is displayed")

            help_button = wait.until(EC.visibility_of_element_located((By.XPATH, selectionsPaths.HomePageTopNav.helpBtn)))
            assert help_button.is_displayed(), "Help button not found"
            print("Help button is displayed")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_ScrollPageDown(self, driver):
        """Test if the homepage scrolls correctly"""
        try:
            actions = ActionChains(driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_ScrollPageUp(self, driver):
        """Test if the homepage scrolls correctly"""
        try:
            actions = ActionChains(driver)
            actions.send_keys(Keys.PAGE_UP).perform()

        except TimeoutError as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_sign_up_email(self, driver):
        """Test if the user can see the placeholders which defines the text boxes"""

        try:
            wait = WebDriverWait(driver, 20)
            email = wait.until(EC.visibility_of_element_located((By.XPATH, signupform.email_signup)))
            assert email.is_displayed(), "the email text box is not visible"
            print(f"The email text box is visible")

            actual_text = email.get_attribute("placeholder").strip()
            expected_text = "Enter your Email"
            assert actual_text == expected_text, f" Text Mismatch! Expected: '{expected_text}',but got:'{actual_text}'"
            print(" The placeholder text in email text box matches the expected value.")

            if email.is_displayed() and actual_text == expected_text:
                email.send_keys("")
                print(f"Empty string entered")
            else:
                raise ElementNotInteractableException(f"user was unable to click")

        except TimeoutError as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_sign_up_company(self, driver):
        """Test if the user can see the placeholders which defines the text boxes"""
        try:
            wait = WebDriverWait(driver, 20)
            company = wait.until(EC.visibility_of_element_located((By.XPATH, signupform.company_name)))
            assert company.is_displayed(), "Company text box not visible"
            print("text box is visible")

            actual_text = company.get_attribute("placeholder").strip()
            expected_text = "Company Name"
            assert actual_text == expected_text, f" Text Mismatch! Expected: '{expected_text}',but got:'{actual_text}'"
            print("The placeholder text in Company text box matches the expected value.")

            if company.is_displayed() and actual_text == expected_text:
                company.send_keys("")
                print(f"Empty string entered")
            else:
                raise ElementNotInteractableException(f"user was unable to click")

        except TimeoutError as e:
            pytest.fail(f"Test failed dur to: {str(e)}")

    def test_sign_up_fullname(self, driver):
        """Test if the user can see the placeholders which defines the text boxes"""
        try:
            wait = WebDriverWait(driver, 20)
            fullname = wait.until(EC.visibility_of_element_located((By.XPATH, signupform.full_name)))
            assert fullname.is_displayed(), "Company text box not visible"
            print("text box is visible")

            actual_text = fullname.get_attribute("placeholder").strip()
            expected_text = "Full Name"
            assert actual_text == expected_text, f" Text Mismatch! Expected: '{expected_text}',but got:'{actual_text}'"
            print("The placeholder text in Company text box matches the expected value.")

            if fullname.is_displayed() and actual_text == expected_text:
                fullname.send_keys("")
                print(f"Empty string entered")
            else:
                raise ElementNotInteractableException(f"user was unable to click")

        except TimeoutError as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_country_code(self, driver):
        """Test if the user can see the placeholders which defines the text boxes"""
        try:
            wait = WebDriverWait(driver, 20)
            countrycode = wait.until(EC.element_to_be_clickable((By.XPATH, signupform.country_code)))
            assert countrycode.is_displayed(), "did not display country code drop down"

            numberTextbox = wait.until(EC.visibility_of_element_located((By.XPATH, signupform.phone_number)))
            assert numberTextbox.is_displayed(), "did not display text box"

            actual_text = numberTextbox.get_attribute("placeholder").strip()
            expected_text = "Phone Number"
            assert actual_text == expected_text, f" Text Mismatch! Expected: '{expected_text}',but got:'{actual_text}'"
            print("The placeholder text in Company text box matches the expected value.")

            if numberTextbox.is_displayed() and actual_text == expected_text:
                print(f"It is the phone number text box")
            else:
                raise NoSuchElementException("text box not found")

        except TimeoutError as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_email_input(self, driver):
        """Test if the user can input valid email"""
        try:
            wait = WebDriverWait(driver, 20)
            emailAddress = wait.until(EC.visibility_of_element_located((By.XPATH, selectionsPaths.signupform.email_signup)))
            assert emailAddress.is_displayed(), "Not displayed"
            emailAddress.send_keys("sahibzadaabdullah94@gmail.com")
            print("Email entered")

            getDemoBtn = wait.until(EC.element_to_be_clickable((By.XPATH, selectionsPaths.signupform.submit_Btn)))
            getDemoBtn.click()
            print("Clicked the submit button.")

        except TimeoutError as e:
            pytest.fail(f"Test failed due to: {str(e)}")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_companyname_input(self, driver):
        """Test if the user can input valid company name"""
        try:
            wait = WebDriverWait(driver, 20)
            companyname = wait.until(EC.visibility_of_element_located((By.XPATH, selectionsPaths.signupform.company_name)))
            assert companyname.is_displayed(), "Not displayed"
            companyname.send_keys("Funsol Technologies")
            print("Company name entered")

        except TimeoutError as e:
            pytest.fail(f"Test failed due to: {str(e)}")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_fullname_input(self, driver):
        """Test if the user can input valid Full Name"""
        try:
            wait = WebDriverWait(driver, 20)
            fullname = wait.until(EC.visibility_of_element_located((By.XPATH, selectionsPaths.signupform.full_name)))
            assert fullname.is_displayed(), "Not displayed"
            fullname.send_keys("Funsol Technologies")
            print("Company name entered")

        except TimeoutError as e:
            pytest.fail(f"Test failed due to: {str(e)}")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")


# Test suite page for login page

class TestLoginPage:

    def test_loginpage_loads(self, driver):
        """Test for if the login page loads correctly"""
        try:
            driver.get("https://app.hrango.com/#")
            print("Login Page is loaded successfully")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_CardText(self, driver):

        """Verify if it is the Login Page w.r.t Card view text and Animation"""

        try:
            loginAnimation = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selectionsPaths.LoginPage.logo)))
            assert loginAnimation.is_displayed(), "No logo found"
            print("It is a Login Page")

            loginCard = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selectionsPaths.LoginPage.cardText)))
            assert loginCard.is_displayed(), "the text is not visbile"
            print("The text on the card view is displayed")

            actual_card_text = loginCard.text.strip()
            expected_card_text = 'Welcome To HRango'

            assert actual_card_text == expected_card_text, f" Text Mismatch! Expected: '{expected_card_text}',but got:'{actual_card_text}'"
            print(" The text on the card matches the expected value.")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_formText(self, driver):
        """Verify if it is the Login Page w.r.t Form text"""

        try:
            welcomeText = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selectionsPaths.LoginPage.formText)))
            assert welcomeText.is_displayed(), "the text is not visible"
            print("The text above the login form is visible")

            actual_form_text = welcomeText.text.strip()
            expected_form_text = 'Welcome aboard,'

            assert actual_form_text == expected_form_text, f" Text Mismatch! Expected: '{expected_form_text}',but got:'{actual_form_text}'"
            print("The text above the form matches the expected value.")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_formLabels(self, driver):
        """Verify if the labels on the above the text fields are visible"""

        try:
            email_label = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, selectionsPaths.LoginPage.labelEmail)))
            assert email_label.is_displayed(), "The label is not "
            print("The email label is displayed")

            actual_label_text = email_label.text.strip()
            expected_label_text = 'Email'

            assert actual_label_text == expected_label_text, f" Text Mismatch! Expected: '{expected_label_text}',but got:'{actual_label_text}'"
            print("The Email label text is verified.")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_formPlaceholderEmail(self, driver):
        """Verifying if the placeholders are displayed and Matched"""

        try:
            email_textfield = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, selectionsPaths.LoginPage.emailInput)))
            assert email_textfield.is_displayed(), "The input field for Email is not visible"
            print("The input field for Email is visible")

            actual_placeholder_text = email_textfield.get_attribute("placeholder").strip()
            expected_placeholder_text = 'Email'

            assert actual_placeholder_text == expected_placeholder_text, f" Text Mismatch! Expected: '{expected_placeholder_text}',but got: '{actual_placeholder_text}'"
            print("The placeholder is correct and visible")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_PlaceholderPass(self, driver):
        """Verifying if the placeholders are displayed and Matched"""

        try:
            pass_textfield = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, selectionsPaths.LoginPage.passwordInput)))
            assert pass_textfield.is_displayed(), "The input field for password is not visible"
            print("The input field for password is visible")

            actual_placeholder_text = pass_textfield.get_attribute("placeholder").strip()
            expected_placeholder_text = 'Password'

            assert actual_placeholder_text == expected_placeholder_text, f" Text Mismatch! Expected: '{expected_placeholder_text}',but got: '{actual_placeholder_text}'"
            print("The placeholder is correct and visible")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_InputEmailIcon(self, driver):
        """Verify if the Icon for Email is visible"""

        try:
            email_icon = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, selectionsPaths.LoginPage.emailIcon)))
            assert email_icon.is_displayed(), "the email icon is not visible"
            print("Email Icon on the Text field is visible")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_InputPassIcon(self, driver):
        """Verify if the Icon for Email is visible"""

        try:
            password_icon = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, selectionsPaths.LoginPage.passwordIcon)))
            assert password_icon.is_displayed(), "Password icon is not displayed"
            print("Password Eye Icon is displayed")
            password_icon.click()
            print("Icon was clicked")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")

    def test_loginBtn(self, driver):
        """Verify if the login button is visible with text and background"""
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, selectionsPaths.LoginPage.loginBtn)))
            assert login_button.is_displayed(), "Button is not visible"
            print("Login button is visible")

            actual_login_text = login_button.text.strip()
            expected_login_text = 'Login'
            assert actual_login_text == expected_login_text, f"Text Mismatch! Expected: '{expected_login_text}',but got: '{actual_login_text}'"
            print("The text on the login button is correct and visible")

        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")





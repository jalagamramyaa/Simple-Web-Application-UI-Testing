from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

# Path to your ChromeDriver executable (update if not in PATH)
# You can also set this as an environment variable or ensure it's in your PATH.
# If chromedriver is in your PATH, you can remove the service_args and executable_path.
CHROMEDRIVER_PATH = "path/to/your/chromedriver.exe" # Replace with your actual path

def test_successful_login():
    """
    Tests successful login with valid credentials.
    """
    print("Starting successful login test...")
    options = ChromeOptions()
    # options.add_argument("--headless") # Uncomment to run in headless mode (without opening browser UI)
    service = ChromeService(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        print("Navigated to login page.")

        # Find username and password fields and enter credentials
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "submit")

        username_field.send_keys("student")
        password_field.send_keys("Password123")
        print("Entered username and password.")

        submit_button.click()
        print("Clicked submit button.")

        # Verify successful login
        time.sleep(2) # Give some time for the page to load
        expected_url = "https://practicetestautomation.com/logged-in-successfully/"
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Expected URL {expected_url}, but got {actual_url}"
        print("Successfully logged in! Current URL is as expected.")

        success_message = driver.find_element(By.CLASS_NAME, "post-title")
        assert "Logged In Successfully" in success_message.text
        print("Success message 'Logged In Successfully' found.")

        logout_button = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button.is_displayed()
        print("Logout button is displayed.")

        print("Successful login test PASSED!")

    except Exception as e:
        print(f"Test failed: {e}")
        driver.save_screenshot("failed_successful_login.png") # Save screenshot on failure
    finally:
        driver.quit()
        print("Browser closed.")

def test_failed_login_invalid_password():
    """
    Tests failed login with invalid password.
    """
    print("\nStarting failed login (invalid password) test...")
    options = ChromeOptions()
    service = ChromeService(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        print("Navigated to login page.")

        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "submit")

        username_field.send_keys("student")
        password_field.send_keys("wrongPassword") # Invalid password
        print("Entered username and invalid password.")

        submit_button.click()
        print("Clicked submit button.")

        time.sleep(2)
        error_message = driver.find_element(By.ID, "error")
        expected_error_text = "Your username is invalid!" # This specific site returns invalid username error even for wrong password
        assert expected_error_text in error_message.text, f"Expected error '{expected_error_text}', but got '{error_message.text}'"
        print(f"Error message '{error_message.text}' found as expected.")

        print("Failed login (invalid password) test PASSED!")

    except Exception as e:
        print(f"Test failed: {e}")
        driver.save_screenshot("failed_invalid_password_login.png")
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    test_successful_login()
    test_failed_login_invalid_password()

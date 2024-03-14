from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # added based on selenium 4 recommendations
from selenium.webdriver.chrome.options import Options  # added for potential future options customization
from datetime import datetime

# constants
email = "YOUR_EMAIL"

# function to log messages
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{timestamp} - {message}")

# function to click on the english option
def click_english_option(driver):
    try:
        # wait for the english option to be clickable, using a more generic selector or different approach
        english_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'English')]"))  # adjust based on the actual text or attributes
        )
        english_option.click()
        log_message("Selected English from the dropdown.")
    except Exception as e:
        log_message(f"Error selecting English option: {e}")

# function to find the decline button
def find_decline_button(driver):
    try:
        # more reliable identification of the decline button
        decline_button = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'I Decline')]"))  # adjust based on actual button text
        )
        return decline_button
    except Exception as e:
        log_message("Decline button not found within 8 seconds.")
        return None

# adding options for future customization
chrome_options = Options()
# example for future use: chrome_options.add_argument("--headless")  # uncomment to run chrome in headless mode

# initialize the webdriver using chromedrivermanager with updated method
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)  # adjusted for selenium 4
log_message("WebDriver initialized.")

# navigate to tinder's login page
driver.get("https://tinder.com/")
log_message("Navigated to Tinder's login page.")

# attempt to click on the decline button
decline_button = find_decline_button(driver)
if decline_button:
    decline_button.click()
    log_message("Decline button clicked.")
else:
    # if decline button is not found, click on the exit button (svg element)
    log_message("Decline button not found, looking for alternative actions.")

# click on the english option
click_english_option(driver)

# wait for user input to exit
input("Press Enter to exit...\n")

# close the browser
driver.quit()
